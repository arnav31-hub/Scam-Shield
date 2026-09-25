function ResultCard({ result }) {

  return (
    <section className="result-card">

      <div className="risk-section">

  <div>
    <p className="result-label">
      RISK LEVEL
    </p>

    <h2 className={`risk-${result.risk_level.toLowerCase()}`}>
      {result.risk_level}
    </h2>
  </div>

  <div className="score">
    <strong>{result.risk_score}</strong>
    <span>/100</span>
  </div>

</div>

      <div className="flags">

  <h3>
    Detected Red Flags
  </h3>

  {result.detected_flags.length === 0 ? (
    <p>No major red flags detected.</p>
  ) : (
    result.detected_flags.map((flag, index) => (
      <div className="flag" key={index}>

        <div>
          <strong>{flag.category}</strong>

          <div className="matches">
            {flag.matches.join(" • ")}
          </div>
        </div>

      </div>
    ))
  )}

</div>

     <div className="recommendation">

  <h3>
    🛡️ What should you do?
  </h3>

  <p>
    {result.recommendation}
  </p>

</div>

    </section>
  );
}

export default ResultCard; 