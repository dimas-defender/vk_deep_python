from setuptools import setup, Extension

def main():
    setup(
        name="cjson",
        version="1.0.0",
        author="Dmitriy Zhabin",
        ext_modules=[
            Extension('cjson', ['cjson.c'])
        ]
    )

if __name__ == "__main__":
    main()
