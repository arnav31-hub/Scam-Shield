import { useState } from "react";
import "./App.css";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import MessageInput from "./components/MessageInput";
import ResultCard from "./components/ResultCard";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeMessage = async () => {
    if (!message.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);

      setResult({
        error: "Unable to connect to ScamShield server.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <Navbar />

      <main className="container">
      <Hero />

        <MessageInput
          message={message}
          setMessage={setMessage}
          loading={loading}
          analyzeMessage={analyzeMessage}
        />

        {result && !result.error && (
          <ResultCard result={result} />
        )}

        {result?.error && (
          <div className="error">
            ⚠️ {result.error}
          </div>
        )}

      </main>
    </div>
  );
}

export default App;