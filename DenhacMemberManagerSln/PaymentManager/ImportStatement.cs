using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using DenhacClientAPI.Services;
using DenhacClientAPI.ResponseObjects;

namespace PaymentManager
{
    public partial class ImportStatement : Form
    {
        public ImportStatement()
        {
            InitializeComponent();
        }

        private void btn_choosefile_Click(object sender, EventArgs e)
        {
            // Create an instance of the open file dialog box.
            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "Open CSV File";
            openFileDialog1.Filter = "CSV files|*.csv";
            
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                using (StreamReader sr = new StreamReader(openFileDialog1.FileName))
                {
                    txt_filecontents.Text = sr.ReadToEnd();
                }
                lbl_filename.Text = openFileDialog1.FileName;
                btn_import.Enabled = true;
            }
        }

        private void btn_back_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btn_import_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Are you really, really, REALLY sure??", "Confirmation", MessageBoxButtons.YesNo);
            if (result == DialogResult.Yes)
            {
                try
                {
                    var service = (ImportPaypalDataResponse)DenhacService.ImportPaypalDataService(txt_filecontents.Text);
                    if (service.transactionStatus)
                    {
                        btn_import.Enabled = false;
                        lbl_numPayments.Text = service.numPayments.ToString();
                        lbl_numUnappliedPayments.Text = service.numUnapplied.ToString() +  "<---******Enter into Member DB manually ******";
                        lbl_totalDues.Text = service.totalDues.ToString();
                        lbl_paypalfees.Text = service.totalFees.ToString() + " <--- ****** Enter into WaveApps manually ******";

                        Clipboard.SetText(service.response);

                        MessageBox.Show(service.response, "This text has been copied to the clipboard");
                    }
                }
                catch (Exception exception)
                {
                    MessageBox.Show(exception.ToString());
                }
            }
        }
    }
}
