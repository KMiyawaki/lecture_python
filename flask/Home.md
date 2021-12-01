# Flask

[README](../README.md)

---

適当なディレクトリに以下のようにファイルを配置してください。作業ディレクトリを`media2`とします。

全てのファイルはこのリポジトリ内に存在しています。

```cmd
media2
│  hello.py
│  sample01.py
│
└─templates
        index.html
```

`media2`で`hello.py`を実行してください。

```cmd
>python3 hello.py
 * Serving Flask app 'hello' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 365-492-344
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Webブラウザで http://127.0.0.1:5000/ にアクセスしてください。ブラウザに`Hello World`の文字が表示されるはずです。

`python3 hello.py`を実行したターミナルで`Ctrl+C`キーによりプログラムを停止させてください。  
次に`sample01.py`を実行し、同じようにブラウザで http://127.0.0.1:5000/ にアクセスしてください。
名前と年齢を入力し、「実行する」を押すと名前と年齢を連結した文字列がブラウザに表示されます。

```cmd
>python3 sample01.py
 * Serving Flask app 'sample01' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 365-492-344
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

---

[README](../README.md)
