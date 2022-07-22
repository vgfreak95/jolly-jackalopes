
# Install conda

* To install conda follow these instructions: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html
* NOTE: you will only need miniconda but anaconda will work as well

# Create Environment

## Create from environment.yml

1. To create the basic environment run

    ```console
    conda create -f environment.yml
    ```

2. To activate the new environment

    ```console
    conda activate jolly
    ```

3. To download the dev dependencies run

    * We are keeping the dev dependencies separate so we will be able to create
    an environment with just the necessary dependencies for running the application

    ```console
    conda install --file dev-requirements.txt
    ```

# Installing Additional Dependencies

1. Activate your environment

    ```console
    conda activate jolly
    ```

2. Attempt conda install

    ```console
    conda install <PACKAGENAME>
    ```

    * If that fails then try searching for the package name if it is slightly
    different with:

    ```console
    conda search <PACKAGENAME>
    ```

3. Attempt pip install
    * Only attempt this if conda install failed

    ```console
    pip install <PACKAGENAME>
    ```

4. Add to corresponding file

    * If it is a dev dependency then add to dev-requirements.txt

    * If it is not a dev dependency export updated environment

    ```console
    conda env export > environment.yml
    ```

5. Commit and push updated environment.yml file

# Update Environment

1. Ensure you have the conda environment you wish to update active

    ```console
    conda activate jolly
    ```

2. Simply run the following command:

    ```console
    conda env update --file environment.yml
    ```
