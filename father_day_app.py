import streamlit as st

st.set_page_config(
    page_title="Father's Day Card",
    page_icon="🎁",
    layout="centered",
)

st.markdown(
    """
    <style>
    body {
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #2f1d4c;
        background: #f5eefc;
    }

    [data-testid='stAppViewContainer'] {
        background: linear-gradient(180deg, #fff8fb 0%, #f3e5ff 100%);
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
    }

    .card-shell {
        position: relative;
        width: min(860px, 100%);
        background: #ffffff;
        border-radius: 32px;
        border: 1px solid rgba(170, 114, 255, 0.25);
        box-shadow: 0 44px 100px rgba(112, 45, 172, 0.12);
        overflow: hidden;
    }

    .hero {
        padding: 3rem 2.5rem 2rem;
        text-align: center;
        position: relative;
        z-index: 1;
    }

    .hero-gradient {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at top, rgba(196, 144, 255, 0.22), transparent 45%);
        pointer-events: none;
    }

    .hero-tag {
        display: inline-flex;
        padding: 0.75rem 1.3rem;
        border-radius: 999px;
        background: rgba(182, 109, 255, 0.16);
        color: #5a2d96;
        font-weight: 700;
        letter-spacing: 0.08em;
        font-size: 0.95rem;
    }

    .hero-title {
        margin: 1rem 0 0;
        font-size: clamp(3rem, 5vw, 4.6rem);
        color: #331f59;
        line-height: 1.02;
    }

    .hero-subtitle {
        margin: 1.4rem auto 0;
        max-width: 680px;
        color: #533f76;
        font-size: 1.05rem;
        line-height: 1.8;
    }

    .card-grid {
        display: grid;
        grid-template-columns: 1.03fr 0.97fr;
        gap: 1.5rem;
        padding: 2rem 2.5rem 3rem;
    }

    .panel {
        position: relative;
        border-radius: 32px;
        background: #fbf2ff;
        border: 1px solid rgba(183, 125, 255, 0.3);
        box-shadow: 0 24px 55px rgba(106, 41, 151, 0.12);
        padding: 2rem;
        overflow: hidden;
        backdrop-filter: blur(4px);
    }

    .panel::before {
        content: '';
        position: absolute;
        width: 100%;
        height: 90px;
        top: 0;
        left: 0;
        background: linear-gradient(180deg, rgba(179, 110, 255, 0.12), transparent 100%);
        z-index: 0;
    }

    .panel::after {
        content: '';
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-image: radial-gradient(circle at 20% 20%, rgba(255,255,255,0.35) 0%, transparent 25%),
                          radial-gradient(circle at 80% 80%, rgba(255,255,255,0.28) 0%, transparent 18%);
        opacity: 0.7;
        pointer-events: none;
        z-index: 0;
    }

    .panel h2 {
        margin: 0;
        color: #431f72;
        font-size: 1.95rem;
        z-index: 1;
        position: relative;
    }

    .panel h2::after {
        content: '';
        display: block;
        width: 70px;
        height: 4px;
        background: linear-gradient(90deg, #9455ff, #d097ff);
        border-radius: 999px;
        margin-top: 0.85rem;
    }

    .panel p {
        margin: 1.25rem 0 0;
        color: #533f76;
        line-height: 1.85;
        z-index: 1;
        position: relative;
    }

    .panel .note {
        margin-top: 1.6rem;
        padding: 1.5rem 1.6rem;
        background: rgba(243, 234, 255, 0.92);
        border-radius: 24px;
        border: 1px solid rgba(162, 99, 255, 0.24);
        z-index: 1;
        position: relative;
    }

    .panel .note strong {
        display: block;
        color: #573d9d;
        margin-bottom: 0.75rem;
    }

    .features {
        margin-top: 1.75rem;
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }

    .feature {
        padding: 1rem 1.1rem;
        border-radius: 22px;
        background: rgba(255, 247, 255, 0.95);
        border: 1px solid rgba(178, 133, 255, 0.24);
        text-align: center;
        color: #4c2f7c;
        font-weight: 700;
    }

    .signature {
        margin-top: 2rem;
        color: #4c2f7c;
        font-weight: 700;
        letter-spacing: 0.04em;
        text-align: right;
        z-index: 1;
        position: relative;
    }

    .heart {
        display: block;
        margin: 2rem auto 0;
        width: fit-content;
        font-size: 3rem;
        animation: pulse 1.2s ease-in-out infinite;
        z-index: 1;
        position: relative;
    }

    .action {
        text-align: center;
        margin-top: 1.5rem;
        z-index: 1;
        position: relative;
    }

    .action button {
        border: none;
        background: linear-gradient(135deg, #7d4cff, #c77bff);
        color: white;
        padding: 0.95rem 1.8rem;
        border-radius: 999px;
        font-size: 1rem;
        font-weight: 700;
        cursor: pointer;
        box-shadow: 0 18px 30px rgba(125, 65, 255, 0.2);
    }

    .open-note-panel {
        margin-top: 1.5rem;
        border-radius: 28px;
        background: rgba(246, 236, 255, 0.95);
        border: 1px solid rgba(168, 104, 255, 0.35);
        padding: 1.8rem;
        box-shadow: 0 20px 40px rgba(90, 39, 142, 0.1);
    }

    .open-note-panel h2 {
        margin: 0 0 0.75rem;
        color: #432c75;
    }

    .open-note-panel p {
        margin: 0.9rem 0 0;
        color: #4a3870;
        line-height: 1.8;
    }

    .open-note-panel .signature {
        margin-top: 1.5rem;
        color: #5a3e8c;
        font-weight: 700;
    }

    .card-edge {
        position: absolute;
        top: 24px;
        left: 24px;
        width: 84%;
        height: 2.2rem;
        background: rgba(255,255,255,0.55);
        transform: rotate(-1deg);
        border-radius: 999px;
        filter: blur(0.5px);
    }

    .card-edge.bottom {
        top: auto;
        bottom: 24px;
        left: auto;
        right: 24px;
        width: 62%;
        height: 2.4rem;
        transform: rotate(2deg);
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.08); }
    }

    @media (max-width: 860px) {
        .card-grid {
            grid-template-columns: 1fr;
        }

        .hero {
            padding: 2rem 1.8rem 1.2rem;
        }

        .card-inner {
            padding: 1.5rem 1.8rem 2rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card-shell">
      <div class="card-edge"></div>
      <div class="hero">
        <div class="hero-tag">Father's Day Card</div>
        <h1 class="hero-title">A Special Card for Dad</h1>
        <p class="hero-subtitle">From far away, Nivedhitha sends this heartfelt greeting to the best father. It is designed to feel warm, personal, and like a real card made just for him.</p>
      </div>
      <div class="card-grid">
        <div class="panel">
          <h2>Beautiful greeting</h2>
          <p>Dad, you are the calm in my storms, the encouragement in every challenge, and the reason I keep chasing my dreams. This card is a small token of how much I miss you.</p>
          <div class="features">
            <div class="feature">Warm wishes</div>
            <div class="feature">A loving note</div>
          </div>
          <div class="heart">💜</div>
        </div>
        <div class="panel">
          <h2>Message from afar</h2>
          <p>Even though I am far away for my studies, my heart is with you today. I hope this card brings you joy and reminds you how much you are loved.</p>
          <div class="note">
            <strong>To Dad</strong>
            <p>You inspire me every day. Thank you for your guidance, patience, and all the moments you make special.</p>
          </div>
          <div class="signature">Love, Nivedhitha</div>
        </div>
      </div>
      <div class="action">
        <button onclick="window.location.reload();">Refresh to reveal more</button>
      </div>
      <div class="card-edge bottom"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Show the hidden note", key="hidden_note"):
    st.markdown(
        """
        <div class="open-note-panel">
          <h2>Dear Dad,</h2>
          <p>Though I am studying far away, I am always thinking of you. Your strength, love, and pride inspire me each day, and I hope this card makes your Father’s Day feel very special.</p>
          <p class="signature">Forever your daughter, Nivedhitha</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()
