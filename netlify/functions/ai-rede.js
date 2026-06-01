// machsruhig.de — KI-Text-Helper (Groq + Llama 3.3 70B)
// Master-Function für trauerrede, danksagung, abschiedsbrief
// Privacy: User-Eingaben gehen an Groq Inc. (USA) — Opt-in im Frontend Pflicht

// Sehr einfaches In-Memory-Rate-Limit pro IP (basic, läuft pro Function-Container)
const ipBuckets = new Map();
const RATE_LIMIT_PER_MIN = 10;
const RATE_LIMIT_PER_DAY = 100;

function checkRateLimit(ip) {
  const now = Date.now();
  const bucket = ipBuckets.get(ip) || { minute: [], day: [] };

  // Filter old entries
  bucket.minute = bucket.minute.filter(t => now - t < 60_000);
  bucket.day = bucket.day.filter(t => now - t < 86_400_000);

  if (bucket.minute.length >= RATE_LIMIT_PER_MIN) {
    return { ok: false, reason: 'rate_limit_minute', retryAfter: 60 };
  }
  if (bucket.day.length >= RATE_LIMIT_PER_DAY) {
    return { ok: false, reason: 'rate_limit_day', retryAfter: 86400 };
  }

  bucket.minute.push(now);
  bucket.day.push(now);
  ipBuckets.set(ip, bucket);
  return { ok: true };
}

// System-Prompts pro Type
const SYSTEM_PROMPTS = {
  trauerrede: `Du bist erfahrener Trauerredner und Schreibhelfer für deutsche Bestattungen. Du erstellst aus den Eingaben einer trauernden Person eine zusammenhängende, würdevolle, persönliche Trauerrede.

WICHTIGE REGELN:
- Korrigiere stillschweigend Rechtschreib- und Grammatikfehler in den Eingaben.
- Übernimm Fakten, Anekdoten und Charakter-Beschreibungen aus den Eingaben — niemals erfinden.
- Schreibe in zusammenhängenden Absätzen, nicht als Liste oder mit Zwischenüberschriften.
- Bei Eingaben wie "er war guter Mann der tomatten geliebt hat" → mache daraus: "Er war ein guter Mensch, der seine Tomaten geliebt hat — wer ihn kannte, weiß, wie er stolz durch seinen Garten ging."
- Tonalität strikt einhalten (würdevoll / persönlich / humorvoll). Bei Trauerreden für Kinder/Jugendliche IMMER würdevoll, niemals humorvoll.
- Länge: kurz ≈ 250 Wörter, mittel ≈ 500 Wörter, lang ≈ 800 Wörter.
- Beginne direkt mit der Eröffnung (z.B. "Liebe Trauergemeinde…"), keine Meta-Kommentare ("Hier ist die Rede:" o.ä.).
- Schreibe in der Sprache, die zur Beziehung passt: bei Kind/Enkel das "Du" zum Verstorbenen, bei distanzierterer Beziehung die respektvolle Form.
- Wenn ein Lieblingssatz/Zitat angegeben ist: arbeite ihn organisch ein, nicht als alleinstehenden Block.
- Ende mit Abschiedsformel passend zur Religion/Weltanschauung.
- Keine Floskeln wie "in der schweren Stunde des Abschieds". Konkret bleiben.`,

  danksagung: `Du bist Schreibhelfer für Danksagungen nach einer Beerdigung in Deutschland. Du erstellst eine kurze, würdevolle Danksagung.

REGELN:
- Korrigiere stillschweigend Rechtschreib- und Grammatikfehler.
- Übernimm Fakten und Beziehungsangaben — niemals erfinden.
- Tonalität strikt: formal (Sie-Form, klassisch) / persönlich (Du-Form, warm) / kurz (knapp, sachlich).
- Länge: formal+persönlich ≈ 80–120 Wörter, kurz ≈ 40–60 Wörter.
- Beginne direkt mit dem Text. Keine Meta-Kommentare.
- Wenn Trauerfeier-Datum/-Ort angegeben: würdig erwähnen.
- Schließe mit "Die Angehörigen" / "In stillem Gedenken" o.ä. — passend zur Tonalität.`,

  abschiedsbrief: `Du bist Schreibhelfer für persönliche Abschiedsbriefe. Du polierst den Entwurf einer Person — du erfindest NICHTS dazu, korrigierst nur Sprache und Fluss.

REGELN:
- Korrigiere Rechtschreib- und Grammatikfehler ohne Inhalt zu ändern.
- Erhalte die Stimme und Wortwahl des Schreibers — du polierst, du übernimmst nicht.
- Verändere keine Fakten, Namen, Aussagen.
- Wenn ein Satz unklar formuliert ist: behutsam glätten, aber Bedeutung exakt erhalten.
- Keine zusätzlichen Phrasen, keine "schönen Floskeln" einfügen.
- Antworte nur mit dem polierten Brief, keine Meta-Kommentare.`,
};

function buildUserMessage(type, data) {
  if (type === 'trauerrede') {
    const parts = [];
    parts.push(`Verstorbene Person: ${data.name || '(nicht angegeben)'}`);
    if (data.age) parts.push(`Alter: ${data.age}`);
    parts.push(`Beziehung zum Verstorbenen: ${data.relationship || 'nicht angegeben'}`);
    parts.push(`Religion/Weltanschauung: ${data.religion || 'weltlich'}`);
    parts.push(`Gewünschte Tonalität: ${data.tone || 'wuerdevoll'}`);
    parts.push(`Gewünschte Länge: ${data.length || 'mittel'} (kurz=250W, mittel=500W, lang=800W)`);
    if (data.character) parts.push(`Charakter & Persönlichkeit: ${data.character}`);
    if (data.hobbies) parts.push(`Was die Person liebte / Hobbys: ${data.hobbies}`);
    if (data.memory) parts.push(`Eine persönliche Erinnerung: ${data.memory}`);
    if (data.message) parts.push(`Was die Person uns bedeutet hat: ${data.message}`);
    if (data.quote) parts.push(`Lieblingssatz der Person: ${data.quote}`);
    if (data.selectedQuote || data.customQuote) {
      parts.push(`Optionales Schluss-Zitat: ${data.selectedQuote || data.customQuote}`);
    }
    return parts.join('\n');
  }

  if (type === 'danksagung') {
    const parts = [];
    parts.push(`Verstorbene Person: ${data.name || '(nicht angegeben)'}`);
    parts.push(`Beziehung: ${data.relationship || 'nicht angegeben'}`);
    parts.push(`Tonalität: ${data.tone || 'persönlich'} (formal/persönlich/kurz)`);
    if (data.ceremony) parts.push(`Hinweis zur Trauerfeier: ${data.ceremony}`);
    return parts.join('\n');
  }

  if (type === 'abschiedsbrief') {
    const parts = [];
    if (data.recipient) parts.push(`Empfänger: ${data.recipient}${data.recipientName ? ' (' + data.recipientName + ')' : ''}`);
    if (data.senderName) parts.push(`Absender: ${data.senderName}`);
    parts.push('\n--- Entwurf zum Polieren ---');
    if (data.sagen) parts.push(`Was ich sagen möchte:\n${data.sagen}`);
    if (data.wichtig) parts.push(`Was wichtig ist:\n${data.wichtig}`);
    if (data.praktisches) parts.push(`Praktisches:\n${data.praktisches}`);
    if (data.wuensche) parts.push(`Wünsche:\n${data.wuensche}`);
    if (data.closing) parts.push(`Schlussformel: ${data.closing}`);
    return parts.join('\n\n');
  }

  return JSON.stringify(data);
}

exports.handler = async function (event) {
  // CORS-Headers für Browser-Requests
  const cors = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers: cors };
  }
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: cors, body: JSON.stringify({ error: 'method_not_allowed' }) };
  }

  // Rate-Limit per IP
  const ip = event.headers['x-forwarded-for'] || event.headers['client-ip'] || 'unknown';
  const rl = checkRateLimit(ip.split(',')[0].trim());
  if (!rl.ok) {
    return {
      statusCode: 429,
      headers: cors,
      body: JSON.stringify({ error: rl.reason, retryAfter: rl.retryAfter }),
    };
  }

  let payload;
  try {
    payload = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: 'invalid_json' }) };
  }

  const { type, data } = payload;
  if (!type || !SYSTEM_PROMPTS[type]) {
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: 'invalid_type' }) };
  }
  if (!data || typeof data !== 'object') {
    return { statusCode: 400, headers: cors, body: JSON.stringify({ error: 'invalid_data' }) };
  }

  // Input-Größen-Limit (Schutz gegen Abuse)
  const userMessage = buildUserMessage(type, data);
  if (userMessage.length > 8000) {
    return { statusCode: 413, headers: cors, body: JSON.stringify({ error: 'input_too_large' }) };
  }

  const apiKey = process.env.GROQ_API_KEY;
  if (!apiKey) {
    return {
      statusCode: 500,
      headers: cors,
      body: JSON.stringify({ error: 'api_key_missing', hint: 'GROQ_API_KEY env-var not set in Netlify' }),
    };
  }

  try {
    const groqResp = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [
          { role: 'system', content: SYSTEM_PROMPTS[type] },
          { role: 'user', content: userMessage },
        ],
        temperature: 0.7,
        max_tokens: 2000,
      }),
    });

    if (!groqResp.ok) {
      const errText = await groqResp.text();
      return {
        statusCode: 502,
        headers: cors,
        body: JSON.stringify({ error: 'groq_api_error', status: groqResp.status, detail: errText.slice(0, 500) }),
      };
    }

    const groqData = await groqResp.json();
    const result = groqData.choices?.[0]?.message?.content?.trim();
    if (!result) {
      return { statusCode: 502, headers: cors, body: JSON.stringify({ error: 'groq_empty_response' }) };
    }

    return {
      statusCode: 200,
      headers: { ...cors, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        result,
        model: 'llama-3.3-70b-versatile',
        usage: groqData.usage || null,
      }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      headers: cors,
      body: JSON.stringify({ error: 'function_error', detail: String(err).slice(0, 500) }),
    };
  }
};
