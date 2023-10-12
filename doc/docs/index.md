# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## AAAAAAA

!!! Note
    これはノートです。


:fa-external-link: [MkDocs](http://www.mkdocs.org/)

定義語
:    ここに説明を書きます

Mkdocs とは静的サイトジェネレータです。
コンテンツは基本的に markdown[^1] 形式で記述したソースファイルになります。

[^1]: 文書を記述するための軽量マークアップ言語のひとつ

;)

(tm)

++ctrl+alt+delete++

![type:video](https://www.youtube.com/embed/LXb3EKWsInQ)

<p><iframe src="https://docs.google.com/presentation/d/1dQgbxB6_0kosazzgfk0Gmoa8c7dInfOy_NvZejfpneo/embed?start=false&loop=false&delayms=5000" frameborder="0" width="800" height="600" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe></p>

``` cpp
#include <iostream>
void main() {
  std::cout << "Hello world!" << std::endl;
}
```

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
