# Copyright (C) 2020 Open Source Integrators
# Copyright (C) 2020 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Field Service Mobile",
    "summary": "Field Service Mobile backend support.",
    "license": "AGPL-3",
    "version": "14.0.1.2.0",
    "category": "Field Service",
    "author": "Open Source Integrators",
    "website": "https://github.com/ursais/osi-addons",
    "depends": [
        "fieldservice_stage_server_action",
        "fieldservice_vehicle",
        "fieldservice_sale_order_line",
        "fieldservice_tracking",
        "fieldservice_sign",
        "fieldservice_stock_request",
        "fieldservice_account_analytic",
        "fieldservice_isp_account",
        "fieldservice_project",
        "fieldservice_equipment_stock",
        "fieldservice_maintenance",
        "fieldservice_vehicle_stock",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "data/base_automation.xml",
        "views/res_config_settings.xml",
        "views/fsm_stage_view.xml",
        "views/fsm_order_view.xml",
    ],
    "development_status": "Beta",
    "maintainers": ["wolfhall"],
}
