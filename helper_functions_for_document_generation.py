from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from datetime import datetime


def generate_agreement_of_sale_pdf(
    file_name,
    seller_name,
    seller_father_name,
    seller_age,
    seller_address,
    purchaser_name,
    purchaser_father_name,
    purchaser_age,
    purchaser_address,
    schedule_property,
    sale_amount,
    advance_amount,
    cheque_no,
    bank_name,
    cheque_date,
    balance_amount,
    transaction_end_date,
    purpose_of_sale,
    seller_wife,
    seller_sons_daughters,
    witness_1,
    witness_2,
    previous_owner,
    previous_sale_deed_date,
    previous_sale_doct_no,
    previous_sale_book1_volumne_no,
    previous_sale_page_no_start,
    prev_sale_page_no_end,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>AGREEMENT OF SALE</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Introduction
    intro = (
        f"THIS AGREEMENT FOR SALE is made and executed on this the {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_details = (
        f"Mr. {seller_name} s/o. {seller_father_name}, aged {seller_age} years, residing at {seller_address}, "
        f'Hereinafter called "The SELLER" (which expression shall mean and include his/her legal heirs, '
        "successors, executors, administrators, legal representatives, and assigns) of ONE PART."
    )
    elements.append(Paragraph(seller_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_details = (
        f"Mr. {purchaser_name} s/o {purchaser_father_name}, aged {purchaser_age} years, residing at "
        f'{purchaser_address}, hereinafter referred to as "The PURCHASER" (represented by his power of '
        "attorney, which expression shall include his heirs, successors, executors, administrators, "
        "legal representatives, and assigns) of the OTHER PART."
    )
    elements.append(Paragraph(purchaser_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Property details and conditions
    elements.append(Paragraph("<b>WHEREAS</b>", styles["Normal"]))
    property_details = (
        f'WHEREAS THE SELLER is the absolute owner in possession and enjoyment of the more fully described in the schedule hereunder and hereafter called the "SCHEDULE PROPERTY".\n'
        f"WHEREAS the property more fully described in the schedule hereunder is the self-acquired property of the SELLER, who purchased the same from Mr. {previous_owner} in and by sale deed dated {previous_sale_deed_date} and registered as Doct No. {previous_sale_doct_no} of Book1VolumeNo {previous_sale_book1_volumne_no} Pagenos.{previous_sale_page_no_start} to {prev_sale_page_no_end}, registered on and filed on the file of the Sub-Registrar.\n"
        f"WHEREAS the SELLER is the absolute owner of the property and has been enjoying the same with absolute right and has clear and marketable title to the Schedule Property.\n"
        f"WHEREAS the SELLER, being in need of funds for the purpose of {purpose_of_sale}, has decided to sell the property more fully described in the Schedule hereunder, and the PURCHASER has offered to purchase the same.\n"
        f"WHEREAS the SELLER offered to sell and transfer the schedule property to the PURCHASER for a sale consideration of Rs. {sale_amount} (Rupees {sale_amount} only), and the PURCHASER herein has agreed to purchase the same for the aforesaid consideration on the following terms and conditions."
    )
    elements.append(Paragraph(property_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Agreement Terms
    elements.append(
        Paragraph(f"<b>NOW THIS AGREEMENT WITNESSETH AS FOLLOWS:</b>", styles["Normal"])
    )
    terms = [
        f"The Sale consideration of the Schedule Property is fixed at Rs. {sale_amount} (Rupees {sale_amount} only).",
        f"The PURCHASER has paid a sum of Rs. {advance_amount} (Rupees {advance_amount} only) by cash/cheque/D.D. bearing No {cheque_no}, drawn on {bank_name}, dated {cheque_date} as advance, the receipt of which sum the SELLER hereby acknowledges.",
        f"The balance payment of Rs. {balance_amount} (Rupees {balance_amount} only) will be paid by the PURCHASER to the SELLER at the time of execution of the absolute Sale Deed, thus completing the sale transaction.",
        "The parties herein covenant to complete the Sale transaction and execute the Absolute Sale Deed by the end of the agreed transaction period.",
        "The SELLER confirms with the PURCHASER that he/she has not entered into any agreement for sale, mortgage, or exchange whatsoever with any other person relating to the Schedule Property of this Agreement.",
        "• The SELLER hereby assures the PURCHASER that he/she has absolute power to convey the same and that there are no encumbrances, liens, charges, Government dues, attachments, acquisition, or requisition proceedings, etc.",
        "The SELLER agrees to put the PURCHASER in absolute and vacant possession of the Schedule Property after executing the sale deed and registering the same in the jurisdictional Sub-Registrar's office.",
        "The SELLER covenants with the PURCHASER that he/she shall not do any act, deed, or thing creating any charge, lien, or encumbrance in respect of the Schedule Property during the subsistence of this Agreement.",
        "The SELLER has specifically agreed and covenants with the PURCHASER that he/she shall do all acts, deeds, and things necessary to convey absolute and marketable title to the Schedule Property in favor of the PURCHASER or his nominee.",
        "IT IS AGREED between the parties that all expenses towards Stamp Duty and Registration charges shall be borne by the PURCHASER only.",
        "• The PURCHASER shall have the right to nominate or assign his right under this agreement to any person/persons of his choice, and the SELLER shall execute the Sale Deed as per the terms and conditions of this Agreement in favor of the PURCHASER or his nominee or assignee.",
        f"• The SELLER has agreed to get a consent deed duly executed to this Sale transaction from his/her spouse ({seller_wife}), sons, and daughters ({seller_sons_daughters}) on or before the date of registration of the Sale Deed and assures that they will all join to execute the sale deed in favor of the PURCHASER.",
        "It is hereby expressly provided and agreed by the parties hereto that both parties are entitled to enforce specific performance of the agreement against each other in case of breach of any conditions mentioned in this Agreement.",
        "The original of the 'AGREEMENT' signed by both parties shall be with the PURCHASER, and a copy of the same, similarly signed, shall be with the SELLER.",
    ]

    for term in terms:
        elements.append(Paragraph(term, styles["Normal"]))
        elements.append(Spacer(1, 12))

    # Schedule Property
    elements.append(Paragraph(f"<b>SCHEDULE PROPERTY:</b>", styles["Normal"]))
    elements.append(Paragraph(schedule_property, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Closing
    elements.append(
        Paragraph(
            "IN WITNESS WHEREOF the SELLER and the PURCHASER have signed this Agreement in the presence of the following witnesses:",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Witnesses:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Signed by SELLER: __________________", styles["Normal"]))
    elements.append(
        Paragraph("Signed by PURCHASER: __________________", styles["Normal"])
    )

    # Build PDF
    doc.build(elements)


def generate_flat_sale_deed_pdf(
    file_name,
    seller_details,
    developer_details,
    confirming_party_details,
    purchaser_details,
    property_details,
    total_consideration,
    cheque_details,
    witness_1,
    witness_2,
    place,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>DEED OF SALE OF FLAT</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Date
    date_intro = (
        f"This DEED OF SALE is made and executed at {place} on this {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(date_intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_paragraph = (
        f"{seller_details['name']}, PAN {seller_details['pan']}, EPIC/Passport No. {seller_details['id_no']}, "
        f"Aadhar No. {seller_details['aadhar']}, son/daughter of {seller_details['father']}, "
        f"residing at {seller_details['address']}, by faith {seller_details['faith']}, "
        f"by Occupation {seller_details['occupation']}, by Nationality {seller_details['nationality']}, "
        "hereinafter referred to and called as the “OWNER(S)/VENDOR(S)”."
    )
    elements.append(Paragraph(seller_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    developer_paragraph = (
        f"{developer_details['name']}, PAN {developer_details['pan']}, "
        f"having place of business at {developer_details['business_address']}, "
        f"represented by its Partner(s) {developer_details['partner']}, "
        f"son/daughter of {developer_details['partner_father']}, "
        f"residing at {developer_details['partner_address']}, by faith {developer_details['faith']}, "
        f"by Occupation {developer_details['occupation']}, "
        f"by Nationality {developer_details['nationality']}, "
        "hereinafter referred to and called as the ‘DEVELOPER(s)’"
    )
    elements.append(Paragraph(developer_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    confirming_party_paragraph = (
        f"{confirming_party_details['name']}, PAN {confirming_party_details['pan']}, "
        f"EPIC/Passport No. {confirming_party_details['id_no']}, "
        f"Aadhar No. {confirming_party_details['aadhar']}, "
        f"son/daughter of {confirming_party_details['father']}, "
        f"residing at {confirming_party_details['address']}, by faith {confirming_party_details['faith']}, "
        f"by Occupation {confirming_party_details['occupation']}, "
        f"by Nationality {confirming_party_details['nationality']}, "
        "hereinafter referred to and called as the “CONFIRMING PARTY (IES)”."
    )
    elements.append(Paragraph(confirming_party_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_paragraph = (
        f"{purchaser_details['name']}, PAN {purchaser_details['pan']}, "
        f"EPIC/Passport No. {purchaser_details['id_no']}, "
        f"Aadhar No. {purchaser_details['aadhar']}, "
        f"son/daughter of {purchaser_details['father']}, "
        f"residing at {purchaser_details['address']}, by faith {purchaser_details['faith']}, "
        f"by Occupation {purchaser_details['occupation']}, "
        f"by Nationality {purchaser_details['nationality']}, "
        "hereinafter referred to and called as the “Purchaser (S)”."
    )
    elements.append(Paragraph(purchaser_paragraph, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Terms of Sale
    elements.append(
        Paragraph("<b>NOW THIS DEED WITNESSETH AS UNDER:</b>", styles["Normal"])
    )
    elements.append(
        Paragraph(
            f"In consideration of Rs {total_consideration} (Rupees {total_consideration} only), the entire amount has been received by the Vendor from the Purchaser prior to the execution of this sale deed.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "1. The Vendor hereby sells, conveys and assigns the property absolutely and forever to the Purchaser.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "2. The actual physical possession of the said property has been handed over by the Vendor to the Purchaser.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(
            "3. The Vendor hereby assures the Purchaser that the property is free from all encumbrances.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))

    # Schedule of Property
    elements.append(Paragraph("<b>THE SCHEDULE “A”</b>", styles["Normal"]))
    schedule_details = (
        f"All that piece and parcel of a demarcated self-contained residential flat being No. {property_details['flat_number']} "
        f"on the {property_details['floor']} Floor, in Block {property_details['block']}, having measurement of "
        f"{property_details['size']} sq. ft., with {property_details['amenities']} within the said Complex."
    )
    elements.append(Paragraph(schedule_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Witnesses
    elements.append(
        Paragraph(
            "IN WITNESS WHEREOF the parties hereto have hereunto set and subscribed their respective hands and seals.",
            styles["Normal"],
        )
    )
    elements.append(Spacer(1, 12))
    elements.append(
        Paragraph(f"Signed by the Vendor: __________________", styles["Normal"])
    )
    elements.append(
        Paragraph(f"Signed by the Purchaser: __________________", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))

    # Build PDF
    doc.build(elements)


def generate_land_sale_deed_pdf(
    file_name,
    seller_name,
    seller_father_name,
    seller_age,
    seller_pan,
    seller_address,
    purchaser_name,
    purchaser_father_name,
    purchaser_age,
    purchaser_pan,
    purchaser_address,
    land_details,
    total_consideration,
    cheque_details,
    witness_1,
    witness_2,
):

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>DEED OF SALE</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Introduction
    intro = (
        f"This DEED OF SALE is made and executed on this {datetime.now().strftime('%d')} day "
        f"{datetime.now().strftime('%B')} of {datetime.now().strftime('%Y')}."
    )
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Parties
    elements.append(Paragraph("<b>BETWEEN</b>", styles["Normal"]))
    seller_details = (
        f"Sri {seller_name}, son of {seller_father_name}, aged about {seller_age} years, "
        f"Holding PAN {seller_pan}, residing at {seller_address}, "
        f"hereinafter called the “SELLER”."
    )
    elements.append(Paragraph(seller_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AND</b>", styles["Normal"]))
    purchaser_details = (
        f"Sri {purchaser_name}, son of {purchaser_father_name}, aged about {purchaser_age} years, "
        f"Holding PAN {purchaser_pan}, residing at {purchaser_address}, "
        f"hereinafter called the “PURCHASER”."
    )
    elements.append(Paragraph(purchaser_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Property details and conditions
    elements.append(Paragraph("<b>WHEREAS</b>", styles["Normal"]))
    property_details = (
        f"WHEREAS the SELLER is the absolute owner of the land measuring about {land_details['size']}, "
        f"lying and situated in {land_details['location']}, described in the schedule hereunder referred to as the “SCHEDULE PROPERTY”.\n"
        f"WHEREAS the SELLER is willing to sell the SCHEDULE PROPERTY to the PURCHASER for a total consideration of "
        f"Rs. {total_consideration} (Rupees {total_consideration} only) and the PURCHASER has agreed to purchase the same."
    )
    elements.append(Paragraph(property_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Agreement Terms
    elements.append(
        Paragraph("<b>NOW THIS DEED OF SALE WITNESSETH:</b>", styles["Normal"])
    )
    terms = [
        f"1. The SELLER hereby sells, conveys, transfers, and assigns unto the PURCHASER the SCHEDULE PROPERTY.",
        f"2. The consideration of Rs. {total_consideration} has been received by the SELLER in cash/cheque/bank draft: {cheque_details}.",
        "3. The SELLER warrants that the SCHEDULE PROPERTY is free from all encumbrances, mortgages, and claims.",
        "4. The SELLER agrees to provide vacant possession of the SCHEDULE PROPERTY to the PURCHASER.",
        "5. The SELLER shall execute all necessary documents to perfect the title of the PURCHASER.",
        "6. The SELLER confirms that all taxes related to the property are paid up to the date of this sale.",
        "7. The PURCHASER is entitled to mutation of title in all public records.",
    ]

    for term in terms:
        elements.append(Paragraph(term, styles["Normal"]))
        elements.append(Spacer(1, 12))

    # Schedule of Property
    elements.append(Paragraph("<b>SCHEDULE OF PROPERTY:</b>", styles["Normal"]))
    schedule_details = (
        f"All that piece and parcel of land measuring about {land_details['size']} "
        f"lying and situated in {land_details['location']}, butted and bounded by:\n"
        f"On the North: {land_details['boundaries']['north']}\n"
        f"On the South: {land_details['boundaries']['south']}\n"
        f"On the East: {land_details['boundaries']['east']}\n"
        f"On the West: {land_details['boundaries']['west']}"
    )
    elements.append(Paragraph(schedule_details, styles["Normal"]))
    elements.append(Spacer(1, 12))

    # Closing
    closing = "IN WITNESS WHEREOF the SELLER and the PURCHASER have set their signatures on the day, month and year first above written."
    elements.append(Paragraph(closing, styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph("Signed by the SELLER: __________________", styles["Normal"])
    )
    elements.append(
        Paragraph("Signed by the PURCHASER: __________________", styles["Normal"])
    )
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles["Normal"]))
    elements.append(Paragraph(f"1. {witness_1}", styles["Normal"]))
    elements.append(Paragraph(f"2. {witness_2}", styles["Normal"]))

    # Build PDF
    doc.build(elements)


def generate_non_disclosure_agreement_pdf(file_name, company_name, company_address, employee_name, employee_address, high_court_city):
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(Paragraph("<b>EMPLOYEE NON-DISCLOSURE & NON-COMPETE AGREEMENT</b>", styles['Title']))
    elements.append(Spacer(1, 12))

    # Date
    date_intro = (f"This EMPLOYEE NON-DISCLOSURE & NON-COMPETE AGREEMENT has been entered into this "
                  f"{datetime.now().strftime('%d')} day of {datetime.now().strftime('%B')}, {datetime.now().strftime('%Y')}.")
    elements.append(Paragraph(date_intro, styles['Normal']))
    elements.append(Spacer(1, 12))

    # BETWEEN Clause
    between_clause = (f"BETWEEN\n\n{company_name}, an Indian [Company / Firm / LLP / Partnership] having its registered office at "
                      f"{company_address} (hereinafter called {company_name.split()[0]} which expression unless repugnant "
                      f"to the context shall mean and include its subsidiaries, and its successors and assigns).\n\n"
                      f"AND\n\n{employee_name}, an Employee of {company_name.split()[0]} and residing at "
                      f"{employee_address} (hereinafter referred to as 'Employee' which expression unless repugnant "
                      f"to the context shall include all beneficiaries of the said employee).")
    elements.append(Paragraph(between_clause, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Definitions
    elements.append(Paragraph("<b>1. Definitions</b>", styles['Normal']))
    definitions = (
        "<b>Intellectual Property:</b> Includes existing and future Intellectual Property in the nature of unregistered or "
        "registered rights to any and all patents, copyrights, trademarks, and other confidential and/or proprietary information limited "
        "to that forming part of the subject matter of the agreement, and inclusive of all intellectual property owned by "
        f"{company_name.split()[0]} and/or its subsidiaries, venture partners, and predecessors in interest, arising out of the performance of this agreement "
        "and/or other business arrangements.\n\n"
        "<b>Confidential Information:</b> Confidential information means, trade secrets, know-how, patents, utility models, formulations, "
        "processes/methods of preparation, test data, conducted in-house or through collaborative efforts, and any and all improvements, modifications, "
        "or alterations that may have been effected to the said Confidential Information by the Company. Confidential information includes, but is not limited to:\n"
        "(i) The terms and conditions of this Agreement or any prior agreement; (ii) Company's business plans, strategies, methods, and practices; "
        "(iii) Information about Company's Personnel, products, customers, marketing strategies, services, or future business plans; "
        "(iv) Process information, including data, reports, studies, test data, and practical instructions related to any product."
    )
    elements.append(Paragraph(definitions, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Acknowledgment of Confidentiality
    elements.append(Paragraph("<b>2. Acknowledgment of Confidentiality</b>", styles['Normal']))
    ack_of_confidentiality = (f"{employee_name} hereby acknowledges that the intellectual property and/or confidential "
                              f"information are in the nature of confidential and proprietary information owned by {company_name.split()[0]}.")
    elements.append(Paragraph(ack_of_confidentiality, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Agreement Not to Disclose
    elements.append(Paragraph("<b>3. Agreement Not to Disclose</b>", styles['Normal']))
    agreement_not_to_disclose = (
        f"a. {employee_name} hereby agrees that he/she shall hold in confidence and not use, commercialize, or disclose any "
        f"confidential information or intellectual property except under the terms of employment with {company_name.split()[0]} "
        "or as authorized in writing by the Company.\n\n"
        "b. Even upon assignment of confidential information or intellectual property to the Company, the employee undertakes to use at least "
        "the same degree of care in safeguarding the confidential information as they use in safeguarding their own confidential information."
    )
    elements.append(Paragraph(agreement_not_to_disclose, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Remedies for Breach
    elements.append(Paragraph("<b>4. Remedies for Breach of Confidentiality</b>", styles['Normal']))
    remedies = (
        f"{employee_name} agrees that any disclosure of confidential information prohibited herein or breach of the provisions may result in "
        f"irreparable injury and damage to {company_name.split()[0]}. The Company may seek legal remedies, including preliminary, temporary, "
        "or permanent injunctions, as necessary to protect its interests. The employee agrees to reimburse reasonable legal fees and other costs incurred."
    )
    elements.append(Paragraph(remedies, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Non-Compete Clause
    elements.append(Paragraph("<b>5. Non-Compete</b>", styles['Normal']))
    non_compete = (
        f"{employee_name} agrees not to directly or indirectly compete with the business of {company_name.split()[0]} for a "
        "period of 5 years following the expiration or termination of this agreement, regardless of the cause."
    )
    elements.append(Paragraph(non_compete, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Jurisdiction
    elements.append(Paragraph("<b>6. Jurisdiction</b>", styles['Normal']))
    jurisdiction = (
        f"Any action arising out of or pertaining to this agreement shall be initiated and maintained in a court of competent jurisdiction "
        f"at the High Court of {high_court_city}."
    )
    elements.append(Paragraph(jurisdiction, styles['Normal']))
    elements.append(Spacer(1, 12))

    # General Provisions
    elements.append(Paragraph("<b>7. General Provisions</b>", styles['Normal']))
    general_provisions = (
        "a. This document constitutes the entire agreement between the parties and supersedes all prior communications, whether written or oral.\n\n"
        "b. This Agreement is limited to its terms and may be modified only by writing signed by both parties.\n\n"
        "c. Neither this Agreement nor any rights or obligations inherent in the Company's Confidential Information, trade secrets, or intellectual property may "
        "be transferred without written consent."
    )
    elements.append(Paragraph(general_provisions, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Severability
    elements.append(Paragraph("<b>8. Severability</b>", styles['Normal']))
    severability = (
        "The provisions of this agreement are severable. If any provision is deemed unenforceable, the remaining provisions will remain in full force and effect. "
        "The parties will substitute an enforceable provision that preserves the original intent."
    )
    elements.append(Paragraph(severability, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Force Majeure
    elements.append(Paragraph("<b>9. Force Majeure</b>", styles['Normal']))
    force_majeure = (
        "Neither party will be responsible for any failure to perform its obligations due to causes beyond its control, such as acts of God, war, riots, embargoes, "
        "fire, floods, or accidents."
    )
    elements.append(Paragraph(force_majeure, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Notice
    elements.append(Paragraph("<b>10. Notice</b>", styles['Normal']))
    notice = (
        "All notices and communications required under this agreement shall be in writing and considered delivered if received in person, or 15 days after mailing by registered post."
    )
    elements.append(Paragraph(notice, styles['Normal']))
    elements.append(Spacer(1, 12))

    # Closing
    closing = (
        "IN WITNESS WHEREOF, the parties have executed this Agreement on the date first written above by their duly authorized representatives."
    )
    elements.append(Paragraph(closing, styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"Signed for {company_name}: __________________", styles['Normal']))
    elements.append(Paragraph(f"Signed by {employee_name}: __________________", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("WITNESSES:", styles['Normal']))
    elements.append(Paragraph("1. __________________", styles['Normal']))
    elements.append(Paragraph("2. __________________", styles['Normal']))

    # Build PDF
    doc.build(elements)

# Example data for the agreement
