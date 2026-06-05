from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    pow_protocol = {
        "signals": [
            {
                "title": "Issuer Signal",
                "desc": "Verified organizations issue digital attestations.",
                "badge": True,
            },
            {
                "title": "Peer Signal",
                "desc": "Senior Scouts stake $CAMP to validate work.",
                "peer": True,
            },
            {
                "title": "Technical Signal",
                "desc": "GitHub/GitLab integrations verify real contributions.",
                "technical": True,
            }
        ],

        "recognition": [
            "Sui Builder Program 2025 – Palawan Winner",
            "Commended by Palawan State University",
            "Live MVP using Move smart contracts"
        ],

        "trust_features": [
            "Stake-based validation",
            "Slashing for fraudulent attestations",
            "Merit-only Master Scout system"
        ]
    }

    return render_template("index.html", data=pow_protocol)


if __name__ == "__main__":
    app.run(debug=True)