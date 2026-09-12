from flask import Flask

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>مرحبا بك</title>
<style>
  body {
    margin: 0;
    height: 100vh;
    background: #0b3d91;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Tahoma', 'Arial', sans-serif;
    color: #ffffff;
  }
  h1 {
    font-size: 90px;
    font-weight: 900;
    margin: 0;
    display: flex;
    gap: 8px;
  }
  h1 span {
    display: inline-block;
    opacity: 0;
    transform: rotate(-180deg) scale(0.2);
    transition: all 0.5s ease;
  }
  h1 span.show {
    opacity: 1;
    transform: rotate(0deg) scale(1);
  }
  #timer {
    font-size: 90px;
    font-weight: 900;
    margin-top: 20px;
    color: #ffffff;
  }
</style>
</head>
<body>
  <h1 id="title"></h1>
  <div id="timer">10</div>

  <script>
    // 1) تقسيم النص إلى حروف
    const text = "مرحبا بك";
    const title = document.getElementById('title');
    const spans = [...text].map(ch => {
      const s = document.createElement('span');
      s.textContent = (ch === ' ') ? '\\u00A0' : ch;
      title.appendChild(s);
      return s;
    });

    // 2) الحركة الدائرية المتسلسلة + التكرار
    function play() {
      spans.forEach(s => s.classList.remove('show'));
      spans.forEach((s, i) => {
        setTimeout(() => s.classList.add('show'), i * 350);
      });
      // بعد ظهور آخر حرف ننتظر ثانيتين ثم نعيد
      setTimeout(play, spans.length * 350 + 2000);
    }
    play();

    // 3) الساعة التنازلية
    let t = 10;
    const timer = document.getElementById('timer');
    setInterval(() => {
      t = t > 0 ? t - 1 : 10;
      timer.textContent = t;
    }, 1000);
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
