from backend import LeaveAndLicenseGenerator, NDAGenerator
from helper_functions_for_document_generation import generate_agreement_of_sale_pdf, generate_flat_sale_deed_pdf, generate_land_sale_deed_pdf, generate_non_disclosure_agreement_pdf
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)
@app.post("/generate-lnl-pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    json_object = json.dumps(json_data)
    lease_generator = LeaveAndLicenseGenerator(json_object)
    lease_generator.generate_pdf()
    pdf_output_path = 'leave_and_license_agreement.pdf'
    # Send the generated PDF as a response
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

@app.post("/generate-general-nda-pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    json_object = json.dumps(json_data)
    nda_generator = NDAGenerator(json_object)
    nda_generator.generate_pdf('nda_agreement.pdf')
    pdf_output_path = 'nda_agreement.pdf'
    # Send the generated PDF as a response
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

@app.post("/generate_agreement_of_sale_pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    print(json_data)
    pdf_output_path = 'sale_agreement.pdf'
    json_data['file_name'] = pdf_output_path
    generate_agreement_of_sale_pdf(**json_data)
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

@app.post("/generate_flat_sale_deed_pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    pdf_output_path = 'flat_sale_deed_pdf.pdf'
    json_data['file_name'] = pdf_output_path
    generate_flat_sale_deed_pdf(**json_data)
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

@app.post("/generate_land_sale_deed_pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    pdf_output_path = 'land_sale_deed_pdf.pdf'
    json_data['file_name'] = pdf_output_path
    generate_land_sale_deed_pdf(**json_data)
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

@app.post("/generate_employee_nda_pdf")
async def generate_pdf(request: Request):
    # Parse the JSON data from the request
    json_data = await request.json()
    pdf_output_path = 'employee_nda_pdf.pdf'
    json_data['file_name'] = pdf_output_path
    generate_non_disclosure_agreement_pdf(**json_data)
    return FileResponse(path=pdf_output_path, filename="auto-generated.pdf", media_type="application/pdf")

