# Copyright (C) 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "OSI Payment Method",
    "version": "14.0.1.0.0",
    "author": "Open Source Integrators",
    "summary": "Adds a payment method field to several models and views",
    "category": "Customers",
    "maintainer": "Open Source Integrators",
    "website": "https://github.com/ursais/osi-addons",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "purchase_stock",
        "osi_vendor_reference",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_views.xml",
        "views/purchase_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["osimallen"],
}
