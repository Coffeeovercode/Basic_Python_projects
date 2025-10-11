import os
from PyPDF2 import PdfWriter

def merge_pdfs_in_directory():
    """
    Finds all PDF files in a directory and merges them into a single PDF.
    """
    print("📄 PDF Merger 📄")
    
    # --- Get User Input ---
    directory = input("Enter the path to the folder containing your PDFs: ")

    if not os.path.isdir(directory):
        print(f"❌ Error: The directory '{directory}' does not exist.")
        return

    # --- Find and sort PDF files ---
    pdf_files = sorted([f for f in os.listdir(directory) if f.lower().endswith('.pdf')])

    if not pdf_files:
        print("No PDF files found in this directory.")
        return

    print("\nPDFs found and will be merged in this order:")
    for pdf in pdf_files:
        print(f"  - {pdf}")

    merger = PdfWriter()

    # --- Merge the files ---
    for filename in pdf_files:
        filepath = os.path.join(directory, filename)
        merger.append(filepath)

    # --- Save the output ---
    output_filename = input("\nEnter a name for the merged PDF file (e.g., combined.pdf): ")
    if not output_filename.lower().endswith('.pdf'):
        output_filename += '.pdf'

    output_path = os.path.join(directory, output_filename)
    merger.write(output_path)
    merger.close()

    print(f"\n✅ Success! Merged PDF saved as '{output_filename}' in the same directory.")

# --- Main execution block ---
if __name__ == "__main__":
    merge_pdfs_in_directory()
