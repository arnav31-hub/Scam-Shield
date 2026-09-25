import re


# Words and phrases that are commonly found in scam messages
SCAM_PATTERNS = {
    "Urgency": [
        "urgent",
        "immediately",
        "act now",
        "right now",
        "within 24 hours",
        "last warning",
        "account will be blocked",
        "account will be closed",
    ],

    "Financial Request": [
        "send money",
        "transfer money",
        "pay now",
        "payment required",
        "upi",
        "otp",
        "bank account",
        "credit card",
        "debit card",
    ],

    "Credential Request": [
        "password",
        "pin",
        "cvv",
        "verify your account",
        "verify kyc",
        "kyc update",
        "login",
    ],

    "Prize / Reward": [
        "you won",
        "congratulations",
        "lucky winner",
        "claim your prize",
        "cash prize",
        "reward",
    ],

    "Threat / Fear": [
        "police",
        "legal action",
        "arrest",
        "penalty",
        "fine",
        "blocked",
        "suspended",
    ],
}


def analyze_message(message: str):

    # Convert the message to lowercase.
    # This makes keyword checking easier.
    text = message.lower()

    detected_flags = []

    # Check every scam category
    for category, patterns in SCAM_PATTERNS.items():

        matches = []

        # Check every keyword in the category
        for pattern in patterns:

            if pattern in text:
                matches.append(pattern)

        # If we found something suspicious,
        # save it in the results.
        if matches:
            detected_flags.append({
                "category": category,
                "matches": matches
            })

    # Look for links in the message
    urls = re.findall(
        r"https?://[^\s]+|www\.[^\s]+",
        text
    )

    if urls:
        detected_flags.append({
            "category": "Suspicious Link",
            "matches": urls
        })

    # Calculate the risk score
    score = 0

    for flag in detected_flags:

        category = flag["category"]

        if category == "Urgency":
            score += 15

        elif category == "Financial Request":
            score += 25

        elif category == "Credential Request":
            score += 25

        elif category == "Prize / Reward":
            score += 20

        elif category == "Threat / Fear":
            score += 20

        elif category == "Suspicious Link":
            score += 25

    # Keep the score between 0 and 100
    score = min(score, 100)

    # Convert the score into a risk level
    if score >= 70:
        risk_level = "HIGH"

    elif score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    # Give the user safety advice
    if risk_level == "HIGH":

        recommendation = (
            "Do not click links, share OTP/passwords, "
            "or transfer money. Verify the message through "
            "the organization's official website or app."
        )

    elif risk_level == "MEDIUM":

        recommendation = (
            "Be careful. Verify the sender and information "
            "through an official source before taking action."
        )

    else:

        recommendation = (
            "No major scam indicators were detected, "
            "but always verify unexpected messages."
        )

    # Send the final result back to the API
    return {
        "risk_score": score,
        "risk_level": risk_level,
        "detected_flags": detected_flags,
        "recommendation": recommendation
    }