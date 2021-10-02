A simple script to copy all objects from one bucket to another using Python boto3.

1. Install dependencies via pip in the terminal
2. Create ".env" in the root dir
3. Fill in your personalized environment variables (keys can be copypasted from ".env.template"):
    - AWS access key ID
    - AWS secret access key
    - Source bucket name
    - Target bucket name
4. Run "python copy-bucket.py" in the terminal