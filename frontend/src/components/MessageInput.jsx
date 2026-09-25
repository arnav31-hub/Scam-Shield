function MessageInput({
  message,
  setMessage,
  loading,
  analyzeMessage,
}){
    return (
    <section className="analyzer-card">

      <label>
        Paste your suspicious message
      </label>

      <textarea
        placeholder="Example: URGENT! Your bank account will be blocked..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={analyzeMessage}
        disabled={loading || !message.trim()}
      >
        {loading ? "Analyzing..." : "🔍 Analyze Message"}
      </button>

    </section>
  );
}
export default MessageInput;