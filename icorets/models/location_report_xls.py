import datetime
from odoo import api, models, fields, _


class LocationReportWizard(models.TransientModel):
    _name = 'locations.report'

    def location_report_xlsx(self):
        return self.env.ref('crm_timesheet.location_report_action_xls').report_action(self)
#
# class LocationReport(models.AbstractModel):
#     _name = "report.crm_timesheet.location_report_xls"
#     _inherit = "report.report_xlsx.abstract"

    # def generate_xlsx_report(self, workbook, data, sale_report):
    #     worksheet = workbook.add_worksheet()
    #     token_list = self.search_invnt(sale_report)
    #     for obj in sale_report:
    #
    #         # Formatting For Data in Excel Sheet
    #         date_format = workbook.add_format({'num_format': 'dd/mm/YYYY', 'font': 'Arial', 'align': 'center', 'valign': 'vcenter','font_size': 8,'border': 1})
    #         title_format = workbook.add_format({
    #             'font_size': 8,
    #             'font': 'Arial',
    #             'border': 1,
    #             'align': 'center',
    #             'bg_color': '#ccccff',
    #             'valign': 'vcenter'})
    #         output_format = workbook.add_format({
    #             'font_size': 8,
    #             'font': 'Arial',
    #             'align': 'left',
    #             'border': 1,
    #             'valign': 'vcenter'})
    #         header_format = workbook.add_format({
    #             'font_size': 14,
    #             'font': 'Arial',
    #             'bold': 1,
    #             'align': 'center',
    #             'valign': 'vcenter'})
    #
    #         # Heading for the values in Excel Sheet
    #         worksheet.merge_range('A1:', 'Location Report', header_format)
    #         headers = ['Brand','Category 1','Category 2','Category 3','Function Sport','Gender',
    #                    'Title','Composition / Material','Technology / Features','Event','HSN Code','Style Code',
    #                    'Article Code','EAN Code','ASIN','FSIN','Colour','Size','MRP','GST','IHO Stock', 'Bhiwandi Stock', 'Delhi Stock']
    #
    #         row = 2
    #
    #         for index, value in enumerate(headers):
    #             worksheet.write(row, index, value, title_format)
    #         row = 3
    #         col = 0
    #         # Adding values in Excel sheet from the Dictionary
    #         for token in token_list:
    #             worksheet.write(row, 0, token['Brand'] or ' ', date_format)
    #             worksheet.write(row, 1, token['Category 1'] or ' ', output_format)
    #             worksheet.write(row, 2, token['Category 2'] or ' ', output_format)
    #             worksheet.write(row, 3, token['Category 3'] or ' ', output_format)
    #             worksheet.write(row, 4, token['Function Sport'] or ' ', date_format)
    #             worksheet.write(row, 5, token['Gender'] or ' ', output_format)
    #             worksheet.write(row, 6, token['Title'] or ' ', date_format)
    #             worksheet.write(row, 7, token['Composition / Material'] or ' ', output_format)
    #             worksheet.write(row, 8, token['Technology / Features'] or ' ', output_format)
    #             worksheet.write(row, 9, token['Event'] or ' ', output_format)
    #             worksheet.write(row, 10, token['HSN Code'] or ' ', output_format)
    #             worksheet.write(row, 11, token['Style Code'] or ' ', output_format)
    #             worksheet.write(row, 12, token['Article Code'] or ' ', output_format)
    #             worksheet.write(row, 13, token['EAN Code'] or ' ', output_format)
    #             worksheet.write(row, 14, token['ASIN'] or ' ', output_format)
    #             worksheet.write(row, 14, token['FSIN'] or ' ', output_format)
    #             worksheet.write(row, 14, token['Colour'] or ' ', output_format)
    #             worksheet.write(row, 14, token['Size'] or ' ', output_format)
    #             worksheet.write(row, 14, token['MRP'] or ' ', output_format)
    #             worksheet.write(row, 14, token['GST'] or ' ', output_format)
    #             worksheet.write(row, 14, token['IHO Stock'] or ' ', output_format)
    #             worksheet.write(row, 14, token['Bhiwandi Stock'] or ' ', output_format)
    #             worksheet.write(row, 14, token['Delhi Stock'] or ' ', output_format)
    #             row = row + 1

    # def search_invnt(self, report_data):
    #     data_list = []
    #
    #     # Domains for filtering according to fields in form view
    #     search_domain = []
    #     # Location Filter
    #     search_domain.append(('location_id.usage','=', 'internal'))
    #
    #     # Filter records according to filters
    #     loc_products = self.env['stock.quant'].search(search_domain)
    #     # Assigning Data in a variable to sort in Dictionary
    #     for inv in loc_products:
    #         inv_dict = self.invoice_dict(inv)
    #         data_list.append(inv_dict)
    #
    #
    #     return data_list

    # Function for Assigning data in a Dictionary
    # def invoice_dict(self, inv):
    #     bom_assy = {
    #         'Brand':inv.product_id.brand_id_rel or '',
    #         'Category 1': inv.product_id.product_tmpl_id.categ_id.name or '',
    #         'Category 2': '',
    #         'Category 3': '',
    #         'Function Sport': inv.product_id.variants_func_spo or '',
    #         'Gender': inv.product_id.gender or '',
    #         'Title': inv.product_id.name or '',
    #         'Composition / Material': inv.product_id.material or '',
    #         'Technology / Features':inv.product_id.variants_tech_feat,
    #         'Event': inv.product_id.occasion or '',
    #         'HSN Code': inv.product_id.l10n_in_hsn_code or inv.product_id.sale_hsn,
    #         'Style Code': inv.product_id.style_code or '',
    #         'Article Code': inv.product_id.variant_article_code or '',
    #         'EAN Code': inv.product_id.barcode or '',
    #         'ASIN': inv.product_id.variants_asin or '',
    #         'FSIN': inv.product_id.variants_fsn or '',
    #         'Colour': inv.product_id.color or '',
    #         'Size': inv.product_id.size or '',
    #         'MRP': inv.product_id.standard_price or '',
    #         'GST': inv.product_id.taxes_id.ids or '',
    #         'IHO Stock': '',
    #         'Bhiwandi Stock': '',
    #         'Delhi Stock': '',
    #     }
    #     return bom_assy


class LocationReport(models.AbstractModel):
    _name = "report.crm_timesheet.location_report_xls"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines):

        bold = workbook.add_format(
            {'font_size': 11, 'align': 'vcenter', 'bold': True, 'bg_color': '#b7b7b7', 'font': 'Calibri Light',
             'text_wrap': True, 'border': 1})
        bold_red = workbook.add_format(
            {'font_size': 11, 'color': '#FF0000', 'align': 'vcenter', 'bold': True, 'bg_color': '#b7b7b7',
             'font': 'Calibri Light',
             'text_wrap': True, 'border': 1})
        bold_one = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bg_color': '#b7b7b7'})
        sheet = workbook.add_worksheet('Location Report')
        sheet.set_column(0, 0, 20)
        sheet.set_column(0, 1, 25)
        sheet.set_column(0, 2, 25)
        sheet.set_column(0, 3, 25)
        sheet.set_column(0, 4, 25)
        sheet.set_column(0, 5, 25)
        sheet.set_column(0, 6, 25)
        sheet.set_column(0, 7, 25)
        sheet.set_column(0, 8, 25)
        sheet.set_column(0, 9, 25)
        sheet.set_column(0, 10, 25)
        sheet.set_column(0, 11, 25)
        sheet.set_column(0, 12, 25)
        sheet.set_column(0, 13, 25)
        sheet.set_column(0, 14, 25)
        sheet.set_column(0, 15, 25)
        sheet.set_column(0, 16, 25)
        sheet.set_column(0, 17, 25)
        sheet.set_column(0, 18, 25)
        sheet.set_column(0, 19, 25)
        sheet.set_column(0, 20, 25)
        sheet.set_column(0, 21, 25)
        sheet.set_column(0, 22, 25)
        sheet.set_column(0, 23, 25)

        # **************************************************
        sheet.write(0, 0, 'Brand', bold)
        sheet.write(0, 1, 'Category 1', bold)
        sheet.write(0, 2, 'Category 2', bold)
        sheet.write(0, 3, 'Category 3', bold)
        sheet.write(0, 4, 'Function Sport', bold)
        sheet.write(0, 5, 'Gender', bold)
        sheet.write(0, 6, 'Title', bold)
        sheet.write(0, 7, 'SKU', bold)
        sheet.write(0, 8, 'Composition / Material', bold)
        sheet.write(0, 9, 'Technology / Features', bold)
        sheet.write(0, 10, 'Event', bold)
        sheet.write(0, 11, 'HSN Code', bold)
        sheet.write(0, 12, 'Style Code', bold)
        sheet.write(0, 13, 'Article Code', bold)
        sheet.write(0, 14, 'EAN Code', bold)
        sheet.write(0, 15, 'ASIN', bold)
        sheet.write(0, 16, 'FSIN', bold)
        sheet.write(0, 17, 'Colour', bold)
        sheet.write(0, 18, 'Size', bold)
        sheet.write(0, 19, 'MRP', bold)
        sheet.write(0, 20, 'GST', bold)
        sheet.write(0, 21, 'IHO Stock', bold)
        sheet.write(0, 22, 'Bhiwandi Stock', bold)
        sheet.write(0, 23, 'Delhi Stock', bold)
        sheet.write(0, 24, 'Available Qty', bold)
        sheet.write(0, 25, 'Reserved Qty', bold)

        row = 1
        col = 0
        product_data = {}

        search_domain = [('location_id.usage', '=', 'internal')]
        stock_q = self.env['stock.quant'].search(search_domain)

        for line in stock_q:
            product_id = line.product_id.id

            if product_id not in product_data:
                product_data[product_id] = {
                    'Brand': line.product_id.brand_id_rel.name or '',
                    'Category 1': line.product_id.categ_id.parent_id.parent_id.name or '',
                    'Category 2': line.product_id.categ_id.parent_id.name or '',
                    'Category 3': line.product_id.categ_id.name or '',
                    'Function Sport': line.product_id.variants_func_spo or '',
                    'Gender': line.product_id.gender or '',
                    'Title': line.product_id.name or '',
                    'SKU Code': line.product_id.default_code or '',
                    'Composition / Material': line.product_id.material or '',
                    'Technology / Features': line.product_id.variants_tech_feat or '',
                    'Event': line.product_id.occasion or '',
                    'HSN Code': line.product_id.l10n_in_hsn_code or line.product_id.sale_hsn.hsnsac_code or '',
                    'Style Code': line.product_id.style_code or '',
                    'Article Code': line.product_id.variant_article_code or '',
                    'EAN Code': line.product_id.barcode or '',
                    'ASIN': line.product_id.variants_asin or '',
                    'FSIN': line.product_id.variants_fsn or '',
                    'Colour': line.product_id.color or '',
                    'Size': line.product_id.size or '',
                    'MRP': line.product_id.lst_price or '',
                    'GST': ''.join([str(x) for x in line.product_id.taxes_id.name]) or '',
                    'IHO Stock': '',
                    'Bhiwandi Stock': '',
                    'Delhi Stock': '',
                    'Available Qty': line.product_id.virtual_available or ''
                }

            # Fill in stock quantities based on location
            if line.location_id.location_id.name == 'IHO':
                product_data[product_id]['IHO Stock'] = line.inventory_quantity_auto_apply
            elif line.location_id.location_id.name == 'BHW':
                product_data[product_id]['Bhiwandi Stock'] = line.inventory_quantity_auto_apply
            elif line.location_id.location_id.name == 'DEL':
                product_data[product_id]['Delhi Stock'] = line.inventory_quantity_auto_apply

        for product_id, data in product_data.items():
            sheet.write(row, col, data['Brand'])
            sheet.write(row, col + 1, data['Category 1'])
            sheet.write(row, col + 2, data['Category 2'])
            sheet.write(row, col + 3, data['Category 3'])
            sheet.write(row, col + 4, data['Function Sport'])
            sheet.write(row, col + 5, data['Gender'])
            sheet.write(row, col + 6, data['Title'])
            sheet.write(row, col + 7, data['SKU Code'])
            sheet.write(row, col + 8, data['Composition / Material'])
            sheet.write(row, col + 9, data['Technology / Features'])
            sheet.write(row, col + 10, data['Event'])
            sheet.write(row, col + 11, data['HSN Code'])
            sheet.write(row, col + 12, data['Style Code'])
            sheet.write(row, col + 13, data['Article Code'])
            sheet.write(row, col + 14, data['EAN Code'])
            sheet.write(row, col + 15, data['ASIN'])
            sheet.write(row, col + 16, data['FSIN'])
            sheet.write(row, col + 17, data['Colour'])
            sheet.write(row, col + 18, data['Size'])
            sheet.write(row, col + 19, data['MRP'])
            sheet.write(row, col + 20, data['GST'])
            sheet.write(row, col + 21, data['IHO Stock'])
            sheet.write(row, col + 22, data['Bhiwandi Stock'])
            sheet.write(row, col + 23, data['Delhi Stock'])
            sheet.write(row, col + 24, data['Available Qty'])

            # Find sales orders related to the product
            sale_orders = self.env['sale.order'].search([('order_line.product_id', '=', product_id)])

            # Calculate 'Qty to Deliver' based on unprocessed sales order quantities
            qty_to_deliver = sum(
                order_line.product_uom_qty for order in sale_orders for order_line in order.order_line if
                not order_line.qty_delivered)

            # Write 'Qty to Deliver'
            sheet.write(row, col + 25, qty_to_deliver)

            row += 1

