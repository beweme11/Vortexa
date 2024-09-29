import json
from pylatex import Document, Tabular, Section, Subsection, Command, Package, NewPage, LongTable, MultiColumn
from pylatex.utils import bold, NoEscape
class LeaveAndLicenseGenerator:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.doc = Document()

    def generate_pdf(self):
        
        self.setup_document()
        self.add_stamp_duty()
        self.add_parties()
        self.add_whereas_clauses()
        self.add_agreement_clauses()
        self.add_schedule()
        self.add_signatures()
        self.doc.generate_pdf('leave_and_license_agreement', clean_tex=False)

    def setup_document(self, font_size='14pt'):
        self.doc.documentclass = Command(
        'documentclass',
        options=[font_size],
        arguments='article'
        )
        self.doc.packages.append(Package('geometry', options=['margin=1in']))
        self.doc.packages.append(Package('array'))
        self.doc.preamble.append(Command('title', 'Leave and License Agreement'))
        self.doc.preamble.append(Command('author', 'Generated Document'))
        self.doc.preamble.append(Command('date', NoEscape(r'\today')))
        self.doc.append(NoEscape(r'\maketitle'))            


    def add_stamp_duty(self):
        with self.doc.create(Tabular('|l|l|l|l|')) as table:
            table.add_hline()
            table.add_row((bold('Particulars'), bold('Amount Paid'), bold('GRN No.'), bold('Date')))
            table.add_hline()
            table.add_row(('Stamp Duty', f"Rs. {self.data['stamp_duty']}/-", self.data['stamp_duty_grn'], self.data['stamp_duty_date']))
            table.add_hline()
            table.add_row(('Registration Fee', f"Rs. {self.data['registration_fee']}/-", self.data['registration_grn'], self.data['registration_date']))
            table.add_hline()

    def add_parties(self):
        with self.doc.create(Section('Parties', numbering=False)):
            self.doc.append(f"This agreement is made and executed on {self.data['date']} at {self.data['city']}")
            self.doc.append('\n\nBetween,\n\n')
            self.doc.append(f"{self.data['licensor_name']}, Age: About {self.data['licensor_age']} Years, ")
            self.doc.append(f"Occupation: {self.data['licensor_occupation']}, ")
            self.doc.append(f"PAN: {self.data['licensor_pan']}, UID: {self.data['licensor_uid']}")
            self.doc.append(f"\nResiding at: {self.data['licensor_address']}")
            self.doc.append('\n\nHEREINAFTER called \'the Licensor\' (which expression shall mean and include the Licensor above named as also his respective heirs, successors, assigns, executors and administrators) \n\nAND\n\n')
            self.doc.append(f"{self.data['licensee_name']}, Age: About {self.data['licensee_age']} Years, ")
            self.doc.append(f"Occupation: {self.data['licensee_occupation']}, ")
            self.doc.append(f"PAN: {self.data['licensee_pan']}, UID: {self.data['licensee_uid']}")
            self.doc.append(f"\nResiding at: {self.data['licensee_address']}")
            self.doc.append('\n\nHEREINAFTER called \'the Licensee\'(which expression shall mean and include only Licensee above named).')

    def add_whereas_clauses(self):
        with self.doc.create(Section('Whereas Clauses', numbering=False)):
            self.doc.append('WHEREAS the Licensor is absolutely seized and possessed of and or otherwise well and ')
            self.doc.append('sufficiently entitled to all that constructed portion being unit described in Schedule ')
            self.doc.append('hereunder written and are hereafter for the sake of brevity called or referred to as ')
            self.doc.append('Licensed Premises and is/are desirous of giving the said premises on Leave and License ')
            self.doc.append('basis under Section 24 of the Maharashtra Rent Control Act, 1999.\n\n')
            self.doc.append('AND WHEREAS the Licensee herein is in need of temporary premises for his use and ')
            self.doc.append('has/have approached the Licensor with a request to allow the Licensee herein to use and ')
            self.doc.append(f"occupy the said premises on Leave and License basis for a period of {self.data['period']} ")
            self.doc.append(f"Months commencing from {self.data['start_date']} and ending on {self.data['end_date']}, ")
            self.doc.append('on terms and subject to conditions hereafter appearing.\n\n')
            self.doc.append('AND WHEREAS the Licensor have agreed to allow the Licensee herein to use and occupy the ')
            self.doc.append('said Licensed premises for his aforesaid purposes only, on Leave and License basis for ')
            self.doc.append('above mentioned period, on terms and subject to conditions hereafter appearing;\n\n')

    def add_agreement_clauses(self):
        with self.doc.create(Section('Agreement Clauses', numbering=False)):
            self.doc.append('NOW THEREFORE IT IS HEREBY AGREED TO, DECLARED AND RECORDED BY AND BETWEEN THE PARTIES HERETO AS FOLLOWS:-\n\n')
            
            # Period
            self.doc.append(bold('1) Period: '))
            self.doc.append(f"That the Licensor hereby grants to the Licensee herein a revocable leave and license, ")
            self.doc.append(f"to occupy the Licensed Premises, described in Schedule hereunder written without creating any ")
            self.doc.append(f"tenancy rights or any other rights, title and interest in favour of the Licensee for a period of ")
            self.doc.append(f"{self.data['period']} Months commencing from {self.data['start_date']} and ending on {self.data['end_date']}\n\n")

            # Rent & Deposit
            self.doc.append(bold('2) Rent & Deposit: '))
            self.doc.append(f"That the Licensee shall pay to the Licensor Rs. {self.data['monthly_rent']} per month towards ")
            self.doc.append(f"the compensation and Rs. {self.data['deposit']} interest free refundable deposit, for the use of ")
            self.doc.append(f"the said licensed premises. The amount of monthly compensation shall be payable within first five ")
            self.doc.append(f"days of the concerned month of Leave and License.\n\n")

            # Payment of Deposit
            self.doc.append(bold('3) Payment of Deposit: '))
            self.doc.append(f"That the Licensee have paid the above mentioned deposit of Rs. {self.data['deposit']} ")
            self.doc.append(f"by {self.data['deposit_payment_method']}.\n\n")

            # Maintenance Charges
            self.doc.append(bold('4) Maintenance Charges: '))
            self.doc.append(f"That the {self.data['maintenance_charges_paid_by']} shall bear and pay all the maintenance charges ")
            self.doc.append(f"in respect of the said Licensed Premises, and other outgoings including all rates, taxes, levies, ")
            self.doc.append(f"assessment, non occupancy charges, etc. in respect of the said premises.\n\n")

            # Use
            self.doc.append(bold('5) Use: '))
            self.doc.append(f"That the Licensed premises shall only be used by the Licensee for {self.data['purpose']} purpose. ")
            self.doc.append(f"The Licensee shall maintain the said premises in its existing condition and damage, if any, caused ")
            self.doc.append(f"to the said premises, the same shall be repaired by the Licensee at its own cost subject to normal ")
            self.doc.append(f"wear and tear. The Licensee shall not do anything in the said premises which is or is likely to cause ")
            self.doc.append(f"a nuisance to the other occupants of the said building or to the prejudice in any manner to the rights ")
            self.doc.append(f"of Licensor in respect of said premises or shall not do any unlawful activities prohibited by State or Central Government.\n\n")

            # Add remaining clauses (6 to 11) similarly...
            self.doc.append(bold('6) Alteration: '))
            self.doc.append("That the Licensee shall not make or permit to be made any alteration or addition to the construction or arrangements (internal or external) of the Licensed premises without obtaining prior written consent from the Licensor.\n\n")

            self.doc.append(bold('7) No Tenancy: '))
            self.doc.append("That the Licensee shall not claim any tenancy rights and shall not have any right to transfer, assign, sublet, or grant any license or sub-license concerning the Licensed premises or any part thereof. Additionally, the Licensee shall not mortgage or raise any loan against the said premises.\n\n")

            self.doc.append(bold('8) Inspection: '))
            self.doc.append("That the Licensor shall have the right to access the Licensed premises, either personally or through an authorized representative, to enter, view, and inspect the premises at reasonable intervals, provided reasonable notice is given to the Licensee.\n\n")

            self.doc.append(bold('9) Cancellation: '))
            self.doc.append("That if the Licensee defaults in making regular and punctual payments of monthly compensation as mentioned herein, or commits a breach of any of the terms, covenants, and conditions of this agreement, or if any legislation prohibiting the Leave and License is imposed, the Licensor shall be entitled to revoke and/or cancel the License granted herein by giving one month's notice in writing. The Licensee shall also have the right to vacate the said premises by providing one month's written notice to the Licensor as mentioned earlier.\n\n")

            self.doc.append(bold('10) Possession: '))
            self.doc.append("That immediately upon the expiration, termination, or cancellation of this agreement, the Licensee shall vacate the said premises without delay along with all personal belongings. In the event that the Licensee fails to remove themselves and/or their belongings from the said premises upon expiry or termination of this Agreement, the Licensor shall be entitled to recover damages at a rate of double the daily amount of compensation per day. Alternatively, the Licensor shall have the right to remove the Licensee and their belongings from the Licensed premises without recourse to the Court of Law.\n\n")

            self.doc.append(bold('11) Registration: '))
            self.doc.append("This Agreement shall be registered, and the Licensee shall bear all expenses related to stamp duty, registration fees, and any incidental charges, if applicable.\n\n")

    def add_schedule(self):
        with self.doc.create(Section('Schedule', numbering=False)):
            self.doc.append('All that constructed portion being residential unit bearing ')
            self.doc.append(f"{self.data['flat_number']}, Built-up Area: {self.data['built_up_area']}, ")
            self.doc.append(f"situated on the {self.data['floor']} Floor of a Building known as {self.data['building_name']} ")
            self.doc.append(f"standing on the plot of land bearing {self.data['plot_details']}, ")
            self.doc.append(f"of Village: {self.data['village']}, situated within the revenue limits of ")
            self.doc.append(f"Tehsil {self.data['tehsil']} and Dist {self.data['district']} and situated within ")
            self.doc.append(f"the limits of {self.data['municipal_corporation']} Municipal Corporation.\n\n")

    def add_signatures(self):
        with self.doc.create(Section('Signatures', numbering=False)):
            self.doc.append('IN WITNESS WHEREOF the parties hereto have set and subscribed their respective signatures ')
            self.doc.append('by way of putting thumb impression electronic signature hereto in the presence of witness, ')
            self.doc.append('who are identifying the executants, on the day, month and year first above written.\n\n')

            # Create a table for signatures
            with self.doc.create(LongTable("| p{0.25\\textwidth} | p{0.25\\textwidth} | p{0.25\\textwidth} | p{0.25\\textwidth} |")) as table:
                table.add_hline()
                table.add_row((MultiColumn(4, align='|c|', data='Signatures'),))
                table.add_hline()
                table.add_row(('Name & Address', 'Photo', 'Thumb Impression', 'Digitally Signed'))
                table.add_hline()
                table.add_row(('Licensee', '', '', ''))
                table.add_row((f"Name: {self.data['licensee_name']}", '', '', ''))
                table.add_row((f"UID: {self.data['licensee_uid']}", '', '', ''))
                table.add_row((f"Address: {self.data['licensee_address']}", '', '', ''))
                table.add_hline()
                table.add_row(('Licensor', '', '', ''))
                table.add_row((f"Name: {self.data['licensor_name']}", '', '', ''))
                table.add_row((f"UID: {self.data['licensor_uid']}", '', '', ''))
                table.add_row((f"Address: {self.data['licensor_address']}", '', '', ''))
                table.add_hline()

# Usage
json_data = '''
{
    "date": "September 27, 2024",
    "city": "Mumbai",
    "stamp_duty": 5000,
    "stamp_duty_grn": "GRN123456",
    "stamp_duty_date": "2024-09-15",
    "registration_fee": 1000,
    "registration_grn": "GRN654321",
    "registration_date": "2024-09-16",
    "licensor_name": "John Doe",
    "licensor_age": "45",
    "licensor_occupation": "Business",
    "licensor_pan": "ABCDE1234F",
    "licensor_uid": "1234 5678 9012",
    "licensor_address": "123 Main St, Mumbai",
    "licensee_name": "Jane Smith",
    "licensee_age": "30",
    "licensee_occupation": "Software Engineer",
    "licensee_pan": "FGHIJ5678K",
    "licensee_uid": "9876 5432 1098",
    "licensee_address": "456 Park Ave, Mumbai",
    "period": "11",
    "start_date": "October 1, 2024",
    "end_date": "August 31, 2025",
    "monthly_rent": "25000",
    "deposit": "100000",
    "deposit_payment_method": "NEFT",
    "maintenance_charges_paid_by": "Licensee",
    "purpose": "residential",
    "flat_number": "A-101",
    "built_up_area": "1000 sq ft",
    "floor": "1st",
    "building_name": "Sunshine Apartments",
    "plot_details": "Plot No. 45, Sector 10",
    "village": "Andheri",
    "tehsil": "Andheri",
    "district": "Mumbai Suburban",
    "municipal_corporation": "Mumbai"
}
'''

class NDAGenerator:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.doc = Document()

    def generate_pdf(self, output_path=None):
        self.setup_document()
        self.add_title()
        self.add_parties()
        self.add_whereas()
        self.add_agreement_clauses()
        self.add_signatures()


        if output_path is None:
            output_path = 'non_disclosure_agreement.pdf'
        
        self.doc.generate_pdf(output_path.rsplit('.', 1)[0], clean_tex=False)
        print(f"PDF generated and saved as: {output_path}")

    def setup_document(self):
        self.doc.packages.append(Package('geometry', options=['margin=1in']))
        self.doc.packages.append(Package('enumitem'))
        self.doc.preamble.append(Command('title', bold('Non-Disclosure Agreement')))
        self.doc.preamble.append(Command('date', NoEscape(r'\today')))

    def add_title(self):
        self.doc.append(NoEscape(r'\maketitle'))
        self.doc.append(NoEscape(r'\thispagestyle{empty}'))
        self.doc.append(f"This non-disclosure agreement (\"Agreement\") is dated {self.data['effective_date']} (\"Effective Date\") and is entered into by and between: \n\n")

    def add_parties(self):
        self.doc.append(self.data['party1_name'] + f" (\"Party 1\")\n\n")
        self.doc.append("AND\n\n")
        self.doc.append(self.data['party2_name'] + f" (\"Party 2\")\n\n")
        self.doc.append("Party 1 and Party 2 are hereinafter referred to individually as a \"Party\" and collectively as the \"Parties\". Wherever the context requires, the Party disclosing the confidential information shall be referred to as the \"Disclosing Party\" and the Party receiving the confidential information shall be referred to as the \"Receiving Party\".")

    def add_whereas(self):
        with self.doc.create(Section('Whereas:', numbering=False)):
            self.doc.append(f"A. Party 1 engages in {self.data['party1_business']} and Party 2 engages in {self.data['party2_business']}.\n")
            self.doc.append(f"B. The Parties wish to collaborate and enter into discussions for the purpose of {self.data['purpose']} (\"Purpose\") and wish to keep such discussions confidential.\n")

    def add_agreement_clauses(self):
        self.doc.append("Now therefore, in consideration for the mutual promises and covenants set forth herein, the Parties agree as follows:")
        
        clauses = [
            "\"Confidential Information\" shall mean and include all non-public information, written or oral, disclosed, directly or indirectly, through any means of communication or observation (including oral, graphic, written or electronic form) by the Disclosing Party or any of its affiliates or representatives to or for the benefit of the Receiving Party from the Effective Date, irrespective of whether such information: (a) has been specifically marked as \"confidential\" at the time of disclosure; (b) is treated as proprietary information by the Disclosing Party; or (c) is owned or developed by the Disclosing Party.",
            "Confidential Information shall include any financial, business, proprietary or technical information of the Disclosing Party.",
            "All such Confidential Information shared under this Agreement shall be used by the Parties exclusively for the Purpose and neither Party shall disclose or otherwise use the Confidential Information for any other purpose or in any other manner without the prior written approval of the Disclosing Party.",
            "The Confidential Information shared under this Agreement may be disclosed by the Receiving Party to other employees on a need to know basis, with written consent from the Disclosing Party, in connection with the Purpose, and who shall protect the Confidential Information in accordance with the terms of this Agreement.",
            "The Receiving Party shall protect the Confidential Information in the same manner as it would protect its own confidential information.",
            "The confidentiality obligations under this Agreement shall not apply to Confidential Information which:",
            "Notwithstanding anything to the contrary contained in this Agreement, Confidential Information may be disclosed as required by applicable law, regulations or governmental procedure, provided the Receiving Party notifies the Disclosing Party prior to such disclosure, unless prohibited by law, so as to afford the Disclosing Party reasonable opportunity to object or seek an appropriate protective order with respect to such disclosure.",
            "The Receiving Party agrees not to issue or release for publication any articles or advertising or publicity matter relating to this Agreement which mention or imply the name of the Disclosing Party any of its affiliates, or subject matter hereof, unless prior written consent is granted by the Disclosing Party subject only to Clause 7. The Receiving Party shall make such amendments to any such press release or public statement as are reasonably requested by the Disclosing Party.",
            "No transfer of intellectual property right either by way of assignment or license is either granted or implied by the disclosure of Confidential Information to the Receiving Party. The fact that Confidential Information is disclosed to the Receiving Party shall not be deemed to constitute any representation, warranty or inducement by the Disclosing Party of any kind (including of its accuracy or correctness) with respect to the Confidential Information, including without limitation, which such use will not infringe on intellectual property rights of any third party.",
            "The Receiving Party shall, upon the request of the Disclosing Party or upon the termination of this Agreement, return to the Disclosing Party all Confidential Information, including drawings, documents, reports and other tangible manifestations of Confidential Information received by the Receiving Party pursuant to this Agreement, together with all copies and reproductions thereof.",
            f"This Agreement shall be effective as of the Effective Date and shall terminate on the delivery of written notice of termination from either Party; provided, however, that the obligations of the Receiving Party under this Agreement shall remain in effect for a period of {self.data['confidentiality_period']} years from the date of termination.",
            f"This Agreement shall be governed and construed in accordance with the laws of India. The competent courts at {self.data['jurisdiction']} India shall have the sole and exclusive jurisdiction over any dispute that arises in relation to this Agreement.",
            "The Partner represents and covenants that its performance of this Agreement does not and will not breach any agreement it has entered into or will enter into with any third party. The Partner agrees not to enter into any written or oral agreement that conflicts with the provisions of this Agreement.",
            "The individuals executing this Agreement represent and warrant that they are empowered and duly authorized execute this Agreement on behalf of the parties they represent. Each Party represents and warrants to the other Party that it is authorised to execute this Agreement and is competent to discharge the obligations under this Agreement.",
            "Nothing in this Agreement will be construed to create a partnership, joint venture, franchise, fiduciary, employment or agency relationship between the parties. Neither Party has any express or implied authority to assume or create any obligations on behalf of the other or to bind the other to any contract, agreement or undertaking with any third party.",
            "If any provision of this Agreement shall be held by a court of competent jurisdiction to be illegal, invalid or unenforceable, the remaining provisions shall remain in full force and effect.",
            "This Agreement contains the full and complete understanding of the parties with respect to the subject matter hereof, and supersedes all prior representations and understandings, whether oral or written. This Agreement may be amended only in writing by mutual agreement of the Parties."
        ]

        for i, clause in enumerate(clauses, 1):
            self.doc.append(f"{i}. {clause} \n\n")

    def add_signatures(self):
        self.doc.append("IN WITNESS WHEREOF, the parties have executed this Agreement under seal as of the Effective Date.")
        self.doc.append("\n\n")
        self.doc.append(NoEscape(r'\begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}'))
        self.doc.append(NoEscape(r'\hline'))
        self.doc.append(NoEscape(r'Signature & Name & Designation & Organisation \\'))
        self.doc.append(NoEscape(r'\hline'))
        self.doc.append(NoEscape(r'& & & \\'))
        self.doc.append(NoEscape(r'\hline'))
        self.doc.append(NoEscape(r'\end{tabular}'))

# Usage example
json_data = '''
{
    "effective_date": "September 27, 2024",
    "party1_name": "ABC Corporation",
    "party2_name": "XYZ Ltd.",
    "party1_business": "software development",
    "party2_business": "data analytics",
    "purpose": "exploring potential collaboration in AI-driven analytics",
    "confidentiality_period": "5",
    "jurisdiction": "Mumbai"
}
'''

generator = NDAGenerator(json_data)
generator.generate_pdf('nda_output.pdf')
