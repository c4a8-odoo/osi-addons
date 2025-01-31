# Copyright (C) 2021 - TODAY, Open Source Integrators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Field Service - Agreement - Helpdesk",
    "summary": "Create links between Field Service, Agreements, and Helpdesk",
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "author": "Open Source Integrators",
    "category": "Helpdesk",
    "website": "https://github.com/ursais/osi-addons",
    "depends": [
        "helpdesk_fieldservice",
        "agreement_helpdesk",
        "fieldservice_agreement",
    ],
    "data": ["views/helpdesk_ticket.xml"],
    "installable": True,
    "auto_install": True,
    "development_status": "Beta",
    "maintainers": ["osi-scampbell"],
}
