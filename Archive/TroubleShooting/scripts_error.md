# scripts 에러

```html
arch -arm64 brew install scriptcs
```

- log
    
    ```csharp
    Error: Cannot install under Rosetta 2 in ARM default prefix (/opt/homebrew)!
    To rerun under ARM use:
        arch -arm64 brew install ...
    To install under x86_64, install Homebrew into /usr/local.
    
    (base) jeonsang-eon@jeonsang-eon-ui-MacBookPro WorkSpace % arch -arm64 brew install scriptcs
    
    Warning: scriptcs has been deprecated because it is not maintained upstream!
    ==> Downloading https://ghcr.io/v2/homebrew/core/scriptcs/manifests/0.17.1
    ######################################################################### 100.0%
    ==> Fetching dependencies for scriptcs: mpdecimal, ca-certificates, openssl@3, readline, sqlite, xz, python@3.11 and mono
    ==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/2.5.1
    ######################################################################### 100.0%
    ==> Fetching mpdecimal
    ==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/blobs/sha256:5b1c62c0
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-
    ######################################################################### 100.0%
    ==> Fetching ca-certificates
    ==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/blobs/sha256:a3
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.1.4
    ######################################################################### 100.0%
    ==> Fetching openssl@3
    ==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/blobs/sha256:1ff0549b
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.7
    ######################################################################### 100.0%
    ==> Fetching readline
    ==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:1cbe9a001
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.44.0
    ######################################################################### 100.0%
    ==> Fetching sqlite
    ==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:6f82ff67c5b
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.4.5
    ######################################################################### 100.0%
    ==> Fetching xz
    ==> Downloading https://ghcr.io/v2/homebrew/core/xz/blobs/sha256:05d853bc61d9bf9
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.6_1
    ######################################################################### 100.0%
    ==> Fetching python@3.11
    ==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/blobs/sha256:016f01
    ######################################################################### 100.0%
    Warning: mono has been deprecated because it uses deprecated `openssl@1.1`!
    ==> Downloading https://ghcr.io/v2/homebrew/core/mono/manifests/6.12.0.182-2
    ######################################################################### 100.0%
    ==> Fetching mono
    ==> Downloading https://ghcr.io/v2/homebrew/core/mono/blobs/sha256:7c423e09da160
    ######################################################################### 100.0%
    ==> Fetching scriptcs
    ==> Downloading https://ghcr.io/v2/homebrew/core/scriptcs/blobs/sha256:d25a27968
    ######################################################################### 100.0%
    ==> Installing dependencies for scriptcs: mpdecimal, ca-certificates, openssl@3, readline, sqlite, xz, python@3.11 and mono
    ==> Installing scriptcs dependency: mpdecimal
    ==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/2.5.1
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/f367c2ee08c56b88be0662703a8e4275f8657608a268c8c44e845154b0cea543--mpdecimal-2.5.1.bottle_manifest.json
    ==> Pouring mpdecimal--2.5.1.arm64_ventura.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/mpdecimal/2.5.1: 71 files, 2.2MB
    ==> Installing scriptcs dependency: ca-certificates
    ==> Downloading https://ghcr.io/v2/homebrew/core/ca-certificates/manifests/2023-
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/ee5843c6049b06251f85ff5520afc763b2d62190ebee334b78115b8bebac8885--ca-certificates-2023-08-22-1.bottle_manifest.json
    ==> Pouring ca-certificates--2023-08-22.all.bottle.1.tar.gz
    ==> Regenerating CA certificate bundle from keychain, this may take a while...
    🍺  /opt/homebrew/Cellar/ca-certificates/2023-08-22: 3 files, 221.7KB
    ==> Installing scriptcs dependency: openssl@3
    ==> Downloading https://ghcr.io/v2/homebrew/core/openssl/3/manifests/3.1.4
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/528fccab152aa17857e73f54f268d413bf94e22188c0e4ff17a6c497d2783b88--openssl@3-3.1.4.bottle_manifest.json
    ==> Pouring openssl@3--3.1.4.arm64_ventura.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/openssl@3/3.1.4: 6,496 files, 28.4MB
    ==> Installing scriptcs dependency: readline
    ==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.7
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/14125f7fa4b49853f76160b864f58379d90e52833ffeb8bd0643609bcd7f02a7--readline-8.2.7.bottle_manifest.json
    ==> Pouring readline--8.2.7.arm64_ventura.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/readline/8.2.7: 50 files, 1.7MB
    ==> Installing scriptcs dependency: sqlite
    ==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.44.0
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/b6e7cd31f42971fa5388d696a09f9cc3c6e7c5b49c3d0d49b9324db1a268b203--sqlite-3.44.0.bottle_manifest.json
    ==> Pouring sqlite--3.44.0.arm64_ventura.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/sqlite/3.44.0: 11 files, 4.7MB
    ==> Installing scriptcs dependency: xz
    ==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.4.5
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/4e81fda476fb634a7e1ac650019bfe768a65d6c387015992df4cd75adf9b3fce--xz-5.4.5.bottle_manifest.json
    ==> Pouring xz--5.4.5.arm64_ventura.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/xz/5.4.5: 163 files, 2.6MB
    ==> Installing scriptcs dependency: python@3.11
    ==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.6_1
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/481941c47c71dfeb6fba3057ead9b0bd21f7ca514b815bd8dde7cbeff257b362--python@3.11-3.11.6_1.bottle_manifest.json
    ==> Pouring python@3.11--3.11.6_1.arm64_ventura.bottle.tar.gz
    ==> /opt/homebrew/Cellar/python@3.11/3.11.6_1/bin/python3.11 -Im ensurepip
    ==> /opt/homebrew/Cellar/python@3.11/3.11.6_1/bin/python3.11 -Im pip install -v 
    🍺  /opt/homebrew/Cellar/python@3.11/3.11.6_1: 3,286 files, 61.9MB
    ==> Installing scriptcs dependency: mono
    ==> Downloading https://ghcr.io/v2/homebrew/core/mono/manifests/6.12.0.182-2
    Already downloaded: /Users/jeonsang-eon/Library/Caches/Homebrew/downloads/6d1b9976e99667050b3965575bd897b2bd28ae401a3637ca7299fa179017ee91--mono-6.12.0.182-2.bottle_manifest.json
    ==> Pouring mono--6.12.0.182.arm64_monterey.bottle.2.tar.gz
    🍺  /opt/homebrew/Cellar/mono/6.12.0.182: 3,573 files, 410.9MB
    ==> Installing scriptcs
    ==> Pouring scriptcs--0.17.1.arm64_monterey.bottle.tar.gz
    🍺  /opt/homebrew/Cellar/scriptcs/0.17.1: 38 files, 12.4MB
    ==> Running `brew cleanup scriptcs`...
    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
    ==> `brew cleanup` has not been run in the last 30 days, running now...
    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
    Removing: /Users/jeonsang-eon/Library/Caches/Homebrew/git--2.42.0... (17.8MB)
    Removing: /Users/jeonsang-eon/Library/Caches/Homebrew/Cask/intellij-idea-ce--2023.2.3,232.10072.27.dmg... (887.6MB)
    Warning: Calling the `appcast` stanza is deprecated! Use the `livecheck` stanza instead.
    Please report this issue to the adoptopenjdk/openjdk tap (not Homebrew/brew or Homebrew/homebrew-core), or even better, submit a PR to fix it:
      /opt/homebrew/Library/Taps/adoptopenjdk/homebrew-openjdk/Casks/adoptopenjdk8.rb:9
    
    Removing: /Users/jeonsang-eon/Library/Caches/Homebrew/api-source/Homebrew/homebrew-cask/2dca8b00ea7f32e677b025ef4986a562e668216c/Cask/intellij-idea-ce.rb... (1.6KB)
    Pruned 0 symbolic links and 2 directories from /opt/homebrew
    ```
    

![스크린샷 2023-11-24 오후 6.10.53.png](scripts%20%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5%205b0d1fff271d4f449ad195cf8dd2ac13/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-24_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.10.53.png)

- 참고사이트
    
    [https://stackoverflow.com/questions/57990818/got-unexpected-named-argument-error-when-running-csharp-code-on-visual-studio](https://stackoverflow.com/questions/57990818/got-unexpected-named-argument-error-when-running-csharp-code-on-visual-studio)
    
    [https://copyprogramming.com/howto/got-unexpected-named-argument-error-when-running-csharp-code-on-visual-studio](https://copyprogramming.com/howto/got-unexpected-named-argument-error-when-running-csharp-code-on-visual-studio)
    

github_scriptcs : [https://github.com/scriptcs/scriptcs/issues/1188](https://github.com/scriptcs/scriptcs/issues/1188)

![스크린샷 2023-11-24 오후 6.48.43.png](scripts%20%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5%205b0d1fff271d4f449ad195cf8dd2ac13/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-11-24_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_6.48.43.png)