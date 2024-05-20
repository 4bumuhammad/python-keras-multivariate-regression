# Python : Keras using a multivariate regression or classification approach

&nbsp;

## &#x1F530; Project

Define : <br />
. . .


&nbsp;

## &#x1F530; Begin : 

Creating Directories and File Structures
<pre>
    ❯ pwd
        /Users/.../&lt;project-name&gt;

    ❯ cd &lt;project-name&gt;

    ❯ python -m venv venv

    ❯ source ./venv/bin/activate

    ❯ pip install --no-cache-dir -r requirements.txt




    <!-- ❯ mkdir -p data models utils

    ❯ touch data/__init__.py data/data_loader.py

    ❯ touch models/__init__.py models/prediction_model.py

    ❯ touch utils/__init__.py utils/helper_functions.py

    ❯ touch train.py predict.py -->

    ❯ tree -L 2 -a -I 'README.md|.DS_Store|.git|.gitignore|venv|gambar-petunjuk' ./
        ./
        ├── data
        │   └── boston_housing.csv
        ├── models
        ├── requirements.txt
        └── src
            ├── predict.py
            └── train.py

        3 directories, 4 files
</pre>

&nbsp;

<pre>
    ❯ pip list
    Package                      Version
    ---------------------------- -----------
    absl-py                      2.1.0
    astunparse                   1.6.3
    certifi                      2024.2.2
    charset-normalizer           3.3.2
    flatbuffers                  24.3.25
    gast                         0.5.4
    google-pasta                 0.2.0
    grpcio                       1.64.0
    h5py                         3.11.0
    idna                         3.7
    joblib                       1.4.2
    keras                        3.3.3
    libclang                     18.1.1
    Markdown                     3.6
    markdown-it-py               3.0.0
    MarkupSafe                   2.1.5
    mdurl                        0.1.2
    ml-dtypes                    0.3.2
    namex                        0.0.8
    numpy                        1.26.4
    opt-einsum                   3.3.0
    optree                       0.11.0
    packaging                    24.0
    pandas                       1.3.4
    pip                          22.0.4
    protobuf                     4.25.3
    Pygments                     2.18.0
    python-dateutil              2.9.0.post0
    pytz                         2024.1
    requests                     2.32.1
    rich                         13.7.1
    scikit-learn                 1.4.2
    scipy                        1.13.0
    setuptools                   58.1.0
    six                          1.16.0
    tensorboard                  2.16.2
    tensorboard-data-server      0.7.2
    tensorflow                   2.16.1
    tensorflow-io-gcs-filesystem 0.37.0
    termcolor                    2.4.0
    threadpoolctl                3.5.0
    typing_extensions            4.11.0
    urllib3                      2.2.1
    Werkzeug                     3.0.3
    wheel                        0.43.0
    wrapt                        1.16.0
</pre>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;