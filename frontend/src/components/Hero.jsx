function Hero(){
    return(
        <section className="hero">
          <div className="badge">
            API for detecting common scam indicators in messages
          </div>

          <h1>
            <span className="message-text">Is this message</span>
            <span className="safe-text"> safe?</span>
          </h1>

          <p>
            Paste a suspicious SMS, WhatsApp message, email,
            or job offer and let ScamShield analyze it.
          </p>
        </section>
    )
}
export default Hero