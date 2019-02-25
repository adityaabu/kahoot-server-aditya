# Kahoot Abal-Abal
---
<div style="text-align: center">
Ini adalah sebuah project kelas BATCH I` Makers Institute. Dimana kami mencoba untuk mengimplementasikan backend kahoot menggunakan python dan flask. Project ini masih dalam bentuk ` Prototype`.
</div>

---
## Cara setup :
1. Instal [Visual Studio Code][link vs code] (VS Code).
2. instal [Python][link python].
3. instal [Insomnia REST Client][Insomnia installer] atau [Postman][Postman installer].
4. Buka visual studio code.
5. setting `Command Prompt` sebagai terminal, tutorial bisa di lihat [disini][tutorial cmd].
6. install [python extension][link python extension] di VS Code
7. Buat project folder, di sini saya membuat folder `kahoot`. Kemudian di cmc kita masuk ke folder tersebut.
8. Di `kahoot` kita akan membuat virtual environment. Pada cmd kita masukan _code_ di bawah ini:
    ```
    python -m venv .\
    ```
9. Pada folder `kahoot` akan muncul beberapa folder dan file. Lalu kita masuk ke folder Script untuk mengaktifkan virtual environtment :
    ```
    C:\Users\<your username>\...\Kahoot>cd Scripts
    C:\Users\<your username>\...\Kahoot>Scripts>activate.bat

    ```
10. Anda akan masuk ke dalam virtual environtment (kahoot), lalu kita ke folder `Scripts`
    ```
    (Kahoot) C:\Users\<your username>\...\Kahoot>cd Scripts
    ```
11. Instal `Flask`
    ```
    (Kahoot) C:\Users\...\Kahoot\Scripts>pip install Flask
    ```
12. Setelah `Flask` terinstall kita akan membuat sebuah folder di folder kahoot bernama "projects" lalu dalam folder "projects" kita buat folder "kahoot-server-aditya" dan di dalam folder tersebut buatlah file dengan nama `app.py` , file tersebut akan menjadi wadah untuk kita dalam membuat _backend_ kahoot.

13. Lalu di cmd kita masuk ke folder `kahoot-server-aditya` :
    ```
    (Kahoot) C:\Users\...\Kahoot\projects\kahoot-server-aditya>
    ```
14. Lalu untuk menjalankan flask masukan code di bawah ini di cmd:
    ```
    (Kahoot) C:\Users\...\kahoot-server>set FLASK_APP=app.py
    (Kahoot) C:\Users\...\kahoot-server>set FLASK_ENV=developments
    (Kahoot) C:\Users\...\kahoot-server>set FLASK_DEBUG=on
    (Kahoot) C:\Users\...\kahoot-server>flask run
    ```
    atau kalian dapat membuat file dengan ekstensi .bat di dalam folder `kahoot-server-aditya` misalkan kita namakan activate-flask.bat di dalam file tsb berisi :
    ```
    set FLASK_APP=app.py
    set FLASK_ENV=development
    set FLASK_DEBUG=on
    flask run
    ``` 
    Sehingga kita dapat menjalankan flask dengan memasukkan code dibawah ini di cmd :
    ```
    (Kahoot) C:\Users\...\kahoot-server>activate-flask.bat
    ```
    di cmd akan muncul tampilan sebagai berikut :
    ```
    * Serving Flask app "app.py "
    * Environment: developments
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) # ctrl+ click link
    ```

## Feature from Kahoot Abal-abal
1. Create Quiz : Pada feature ini kita akan membuat quiz
2. Get Quiz : Pada feature ini kita dapat mendapatkan data dari quiz yang kita inginkan
3. Update Quiz : Pada feature ini kita dapat  mengupdate data dari quiz yang kita inginkan
4. Delete Quiz : Pada feature ini kita dapat menghapus data dari quiz yang kita inginkan berserta dengan Question pada quiz tersebut.
5. Create Question : Pada feature ini kita akan membuat quiz
6. Get That Question : Pada feature ini kita dapat mendapatkan data dari Question yang kita inginkan
7. Update Question : Pada feature ini kita dapat  mengupdate data dari Question yang kita inginkan
8. Delete Question : Pada feature ini kita dapat menghapus data dari Question yang kita inginkan.
9. Create Game : Pada feature ini kita akan membuat game
10. Join Game : Pada feature ini kita dapat join game
11. Submit Answer : Pada feature ini kita dapat submit jawaban user
12. Get Leaderboard : Pada feature ini kita mendapatkan Leaderboard
13. Sign Up : Pada feature ini kita dapat Sign Up
14. Sign In : Pada feature ini kita dapat Sign In
15. Encripsi Password : Feature untuk mengenkripsi password dengan menggunakan caesar cipter

[link vs code]:https://code.visualstudio.com/download "Visual Studio Code Stable"
[link python]:https://www.python.org/downloads/ "Python"
[Insomnia installer]:https://insomnia.rest/download/ "Insomnia REST Client"
[Postman installer]:https://www.getpostman.com/downloads/ "Postman"
[link python extension]: https://marketplace.visualstudio.com/items?itemName=ms-python.python/ "Python extension"
[tutorial cmd]: https://medium.com/codingthesmartway-com-blog/getting-started-with-visual-studio-code-5f56eef810e1