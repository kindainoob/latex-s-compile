# LaTeXを１発コンパイルする

- 使用言語
  - Python
- 用途
  - LaTeXをplatex環境で1発コンパイルする
  - タイプセットもok(platexを2回行う)
- 仕様
  - python実行時に引数としたファイル名のtexファイル全てに対しplatexを2回,そこで生成されたdviファイルに対しdvipdfmxを1回行う
  - 終了時に.logや.auxを削除する
- 使い方
  1. texファイルを記述するフォルダ内部にフォルダを作成
  2. 作成したフォルダ内にcompile.pyを配置
  3. compile.py [filename1] [filename2] .... のようにファイルネームを引数として与える([]と拡張子は不要)
  4. 与えたファイル全てに対しコンパイルを行う
  5. 生成されたpdfファイルを親ディレクトリに移動
  6. 終了時にログファイル等を削除する
- 注意
  - 親ディレクトリのファイルに対して行うためtexフォルダ内にフォルダを作成してください
