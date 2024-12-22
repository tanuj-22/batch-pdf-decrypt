import os
from PyPDF2 import PdfReader, PdfWriter

def decrypt_pdfs(input_dir, output_dir, password):
    """
    Decrypts all encrypted PDF files in a given directory using the same password.

    :param input_dir: Directory containing encrypted PDF files.
    :param output_dir: Directory to save decrypted PDF files.
    :param password: Password to decrypt the PDF files.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                reader = PdfReader(input_path)

                if reader.is_encrypted:
                    if reader.decrypt(password):
                        writer = PdfWriter()

                        for page in reader.pages:
                            writer.add_page(page)

                        with open(output_path, "wb") as output_pdf:
                            writer.write(output_pdf)

                        print(f"Decrypted and saved: {filename}")
                    else:
                        print(f"Failed to decrypt: {filename}. Incorrect password.")
                else:
                    print(f"{filename} is not encrypted. Skipping.")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    input_directory = input("Enter the input directory containing encrypted PDF files: ").strip()
    output_directory = input("Enter the output directory to save decrypted files: ").strip()
    pdf_password = input("Enter the password for decryption: ").strip()

    decrypt_pdfs(input_directory, output_directory, pdf_password)
