namespace PaymentManager
{
    partial class ImportStatement
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btn_choosefile = new System.Windows.Forms.Button();
            this.lbl_filename = new System.Windows.Forms.Label();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.txt_filecontents = new System.Windows.Forms.TextBox();
            this.btn_back = new System.Windows.Forms.Button();
            this.btn_import = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.lbl_paypalfees = new System.Windows.Forms.Label();
            this.lbl_totalDues = new System.Windows.Forms.Label();
            this.lbl_numUnappliedPayments = new System.Windows.Forms.Label();
            this.lbl_numPayments = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // btn_choosefile
            // 
            this.btn_choosefile.Location = new System.Drawing.Point(13, 13);
            this.btn_choosefile.Name = "btn_choosefile";
            this.btn_choosefile.Size = new System.Drawing.Size(117, 39);
            this.btn_choosefile.TabIndex = 0;
            this.btn_choosefile.Text = "Choose File";
            this.btn_choosefile.UseVisualStyleBackColor = true;
            this.btn_choosefile.Click += new System.EventHandler(this.btn_choosefile_Click);
            // 
            // lbl_filename
            // 
            this.lbl_filename.AutoSize = true;
            this.lbl_filename.Location = new System.Drawing.Point(137, 25);
            this.lbl_filename.Name = "lbl_filename";
            this.lbl_filename.Size = new System.Drawing.Size(49, 13);
            this.lbl_filename.TabIndex = 1;
            this.lbl_filename.Text = "Filename";
            this.lbl_filename.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // txt_filecontents
            // 
            this.txt_filecontents.Location = new System.Drawing.Point(13, 59);
            this.txt_filecontents.Multiline = true;
            this.txt_filecontents.Name = "txt_filecontents";
            this.txt_filecontents.ReadOnly = true;
            this.txt_filecontents.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txt_filecontents.Size = new System.Drawing.Size(730, 307);
            this.txt_filecontents.TabIndex = 2;
            this.txt_filecontents.Text = "`";
            this.txt_filecontents.WordWrap = false;
            // 
            // btn_back
            // 
            this.btn_back.Location = new System.Drawing.Point(14, 372);
            this.btn_back.Name = "btn_back";
            this.btn_back.Size = new System.Drawing.Size(117, 52);
            this.btn_back.TabIndex = 3;
            this.btn_back.Text = "BACK";
            this.btn_back.UseVisualStyleBackColor = true;
            this.btn_back.Click += new System.EventHandler(this.btn_back_Click);
            // 
            // btn_import
            // 
            this.btn_import.Enabled = false;
            this.btn_import.Location = new System.Drawing.Point(630, 372);
            this.btn_import.Name = "btn_import";
            this.btn_import.Size = new System.Drawing.Size(113, 51);
            this.btn_import.TabIndex = 4;
            this.btn_import.Text = "IMPORT";
            this.btn_import.UseVisualStyleBackColor = true;
            this.btn_import.Click += new System.EventHandler(this.btn_import_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(140, 373);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(138, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "# of Applied Payments:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(140, 386);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(153, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "# of Unapplied Payments:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(140, 399);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(130, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Total Dues Collected:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(140, 412);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(142, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Total Paypal Fees Paid:";
            // 
            // lbl_paypalfees
            // 
            this.lbl_paypalfees.AutoSize = true;
            this.lbl_paypalfees.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_paypalfees.Location = new System.Drawing.Point(303, 412);
            this.lbl_paypalfees.Name = "lbl_paypalfees";
            this.lbl_paypalfees.Size = new System.Drawing.Size(0, 13);
            this.lbl_paypalfees.TabIndex = 12;
            // 
            // lbl_totalDues
            // 
            this.lbl_totalDues.AutoSize = true;
            this.lbl_totalDues.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_totalDues.Location = new System.Drawing.Point(303, 399);
            this.lbl_totalDues.Name = "lbl_totalDues";
            this.lbl_totalDues.Size = new System.Drawing.Size(0, 13);
            this.lbl_totalDues.TabIndex = 11;
            // 
            // lbl_numUnappliedPayments
            // 
            this.lbl_numUnappliedPayments.AutoSize = true;
            this.lbl_numUnappliedPayments.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_numUnappliedPayments.Location = new System.Drawing.Point(303, 386);
            this.lbl_numUnappliedPayments.Name = "lbl_numUnappliedPayments";
            this.lbl_numUnappliedPayments.Size = new System.Drawing.Size(0, 13);
            this.lbl_numUnappliedPayments.TabIndex = 10;
            // 
            // lbl_numPayments
            // 
            this.lbl_numPayments.AutoSize = true;
            this.lbl_numPayments.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_numPayments.Location = new System.Drawing.Point(303, 373);
            this.lbl_numPayments.Name = "lbl_numPayments";
            this.lbl_numPayments.Size = new System.Drawing.Size(0, 13);
            this.lbl_numPayments.TabIndex = 9;
            // 
            // ImportStatement
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(755, 433);
            this.Controls.Add(this.lbl_paypalfees);
            this.Controls.Add(this.lbl_totalDues);
            this.Controls.Add(this.lbl_numUnappliedPayments);
            this.Controls.Add(this.lbl_numPayments);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn_import);
            this.Controls.Add(this.btn_back);
            this.Controls.Add(this.txt_filecontents);
            this.Controls.Add(this.lbl_filename);
            this.Controls.Add(this.btn_choosefile);
            this.Name = "ImportStatement";
            this.Text = "ImportStatement";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_choosefile;
        private System.Windows.Forms.Label lbl_filename;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.TextBox txt_filecontents;
        private System.Windows.Forms.Button btn_back;
        private System.Windows.Forms.Button btn_import;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label lbl_paypalfees;
        private System.Windows.Forms.Label lbl_totalDues;
        private System.Windows.Forms.Label lbl_numUnappliedPayments;
        private System.Windows.Forms.Label lbl_numPayments;
    }
}