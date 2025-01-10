Version=$1
SEMVER=$Version

if [ -z "$2" ]
then
    echo "Bumping package version to $1"

    sed -E "s/current_version = .+/current_version = '$SEMVER'/g" setup.py > tempfile && cat tempfile > setup.py && rm -f tempfile

    echo --------------------------
    echo "Done, Package now at $1"
fi
