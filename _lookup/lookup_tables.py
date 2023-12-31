import json

# Initialize look-up tables
category_id_lookup_file = open(
    'new_spend_tables/categories/idlookup/categories_id_lookup.json')
category_id_lookup = json.load(category_id_lookup_file)

organization_id_lookup_file = open(
    'new_spend_tables/organizations/idlookup/organization_id_lookup.json')
organization_id_lookup = json.load(organization_id_lookup_file)

group_id_lookup_file = open(
    'new_spend_tables/groups/idlookup/groups_id_lookup.json')
group_id_lookup = json.load(group_id_lookup_file)

invite_id_lookup_file = open(
    'new_spend_tables/invites/idlookup/invites_id_lookup.json')
invite_id_lookup = json.load(invite_id_lookup_file)

roster_id_lookup_file = open(
    'new_spend_tables/rosters/idlookup/rosters_id_lookup.json')
roster_id_lookup = json.load(roster_id_lookup_file)

season_id_lookup_file = open(
    'new_spend_tables/seasons/idlookup/seasons_id_lookup.json')
season_id_lookup = json.load(season_id_lookup_file)

budget_item_id_lookup_file = open(
    'new_spend_tables/budget_items/idlookup/budget_items_id_lookup.json')
budget_item_id_lookup = json.load(budget_item_id_lookup_file)

payment_schedule_invoice_id_lookup_file = open(
    'new_spend_tables/payment_schedule_invoices/idlookup/payment_schedule_invoices_id_lookup.json')
payment_schedule_invoice_id_lookup = json.load(payment_schedule_invoice_id_lookup_file)

