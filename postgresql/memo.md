docker exec -it 234b68f46027 /bin/sh
psql -U postgres

Adminer で接続

データベース種類：PostgreSQL
サーバ：db
ユーザ名：postgres
パスワード：example
データベース：postgres

# pip install psycopg2 が失敗

```
kotaro@KotaronoMacBook-puro db_sqlalchemy % pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.9.9.tar.gz (384 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [21 lines of output]
      running egg_info
      writing psycopg2.egg-info/PKG-INFO
      writing dependency_links to psycopg2.egg-info/dependency_links.txt
      writing top-level names to psycopg2.egg-info/top_level.txt

      Error: pg_config executable not found.

      pg_config is required to build psycopg2 from source.  Please add the directory
      containing pg_config to the $PATH or specify the full executable path with the
      option:

          python setup.py build_ext --pg-config /path/to/pg_config build ...

      or with the pg_config option in 'setup.cfg'.

      If you prefer to avoid building psycopg2 from source, please install the PyPI
      'psycopg2-binary' package instead.

      For further information please check the 'doc/src/install.rst' file (also at
      <https://www.psycopg.org/docs/install.html>).

      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
```

これで解決
brew install postgresql

```
kotaro@KotaronoMacBook-puro db_sqlalchemy % pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.9.9.tar.gz (384 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: psycopg2
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.9-cp312-cp312-macosx_12_0_x86_64.whl size=143793 sha256=18af5e01b4c688d1da5e1b79178b724fddb4bfcc10c3b7bdbd531a34769b1956
  Stored in directory: /Users/kotaro/Library/Caches/pip/wheels/ff/ac/80/7ccec163e3d05ae2112311b895132409b9abfd7e0c1c6b5183
Successfully built psycopg2
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.9
```

ProductName: macOS
ProductVersion: 12.3.1
BuildVersion: 21E258
