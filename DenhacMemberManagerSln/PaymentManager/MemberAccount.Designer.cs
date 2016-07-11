namespace PaymentManager
{
    partial class MemberAccount
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
            this.components = new System.ComponentModel.Container();
            this.dgv_memberAccount = new System.Windows.Forms.DataGridView();
            this.lbl_firstName = new System.Windows.Forms.Label();
            this.lbl_lastName = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.lbl_id = new System.Windows.Forms.Label();
            this.lbl_phone = new System.Windows.Forms.Label();
            this.lbl_phone2 = new System.Windows.Forms.Label();
            this.lbl_adusername = new System.Windows.Forms.Label();
            this.lbl_contactemail = new System.Windows.Forms.Label();
            this.lbl_paypalemail = new System.Windows.Forms.Label();
            this.lbl_paymentamount = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.lbl_balance = new System.Windows.Forms.Label();
            this.btn_back = new System.Windows.Forms.Button();
            this.bs_memberaccount = new System.Windows.Forms.BindingSource(this.components);
            this.transactiondateDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.amountDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.typeDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.notesDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dgv_memberAccount)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_memberaccount)).BeginInit();
            this.SuspendLayout();
            // 
            // dgv_memberAccount
            // 
            this.dgv_memberAccount.AutoGenerateColumns = false;
            this.dgv_memberAccount.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgv_memberAccount.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.transactiondateDataGridViewTextBoxColumn,
            this.amountDataGridViewTextBoxColumn,
            this.typeDataGridViewTextBoxColumn,
            this.notesDataGridViewTextBoxColumn});
            this.dgv_memberAccount.DataSource = this.bs_memberaccount;
            this.dgv_memberAccount.Location = new System.Drawing.Point(12, 147);
            this.dgv_memberAccount.Name = "dgv_memberAccount";
            this.dgv_memberAccount.Size = new System.Drawing.Size(649, 382);
            this.dgv_memberAccount.TabIndex = 2;
            // 
            // lbl_firstName
            // 
            this.lbl_firstName.AutoSize = true;
            this.lbl_firstName.Location = new System.Drawing.Point(57, 36);
            this.lbl_firstName.Name = "lbl_firstName";
            this.lbl_firstName.Size = new System.Drawing.Size(52, 13);
            this.lbl_firstName.TabIndex = 3;
            this.lbl_firstName.Text = "Firstname";
            // 
            // lbl_lastName
            // 
            this.lbl_lastName.AutoSize = true;
            this.lbl_lastName.Location = new System.Drawing.Point(139, 36);
            this.lbl_lastName.Name = "lbl_lastName";
            this.lbl_lastName.Size = new System.Drawing.Size(53, 13);
            this.lbl_lastName.TabIndex = 4;
            this.lbl_lastName.Text = "Lastname";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(21, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "ID:";
            // 
            // lbl_id
            // 
            this.lbl_id.AutoSize = true;
            this.lbl_id.Location = new System.Drawing.Point(35, 13);
            this.lbl_id.Name = "lbl_id";
            this.lbl_id.Size = new System.Drawing.Size(31, 13);
            this.lbl_id.TabIndex = 6;
            this.lbl_id.Text = "lbl_id";
            // 
            // lbl_phone
            // 
            this.lbl_phone.AutoSize = true;
            this.lbl_phone.Location = new System.Drawing.Point(335, 36);
            this.lbl_phone.Name = "lbl_phone";
            this.lbl_phone.Size = new System.Drawing.Size(38, 13);
            this.lbl_phone.TabIndex = 7;
            this.lbl_phone.Text = "Phone";
            // 
            // lbl_phone2
            // 
            this.lbl_phone2.AutoSize = true;
            this.lbl_phone2.Location = new System.Drawing.Point(335, 56);
            this.lbl_phone2.Name = "lbl_phone2";
            this.lbl_phone2.Size = new System.Drawing.Size(44, 13);
            this.lbl_phone2.TabIndex = 8;
            this.lbl_phone2.Text = "Phone2";
            // 
            // lbl_adusername
            // 
            this.lbl_adusername.AutoSize = true;
            this.lbl_adusername.Location = new System.Drawing.Point(57, 56);
            this.lbl_adusername.Name = "lbl_adusername";
            this.lbl_adusername.Size = new System.Drawing.Size(73, 13);
            this.lbl_adusername.TabIndex = 9;
            this.lbl_adusername.Text = "AD Username";
            // 
            // lbl_contactemail
            // 
            this.lbl_contactemail.AutoSize = true;
            this.lbl_contactemail.Location = new System.Drawing.Point(111, 76);
            this.lbl_contactemail.Name = "lbl_contactemail";
            this.lbl_contactemail.Size = new System.Drawing.Size(72, 13);
            this.lbl_contactemail.TabIndex = 10;
            this.lbl_contactemail.Text = "Contact Email";
            // 
            // lbl_paypalemail
            // 
            this.lbl_paypalemail.AutoSize = true;
            this.lbl_paypalemail.Location = new System.Drawing.Point(111, 97);
            this.lbl_paypalemail.Name = "lbl_paypalemail";
            this.lbl_paypalemail.Size = new System.Drawing.Size(67, 13);
            this.lbl_paypalemail.TabIndex = 11;
            this.lbl_paypalemail.Text = "Paypal Email";
            // 
            // lbl_paymentamount
            // 
            this.lbl_paymentamount.AutoSize = true;
            this.lbl_paymentamount.Location = new System.Drawing.Point(111, 119);
            this.lbl_paymentamount.Name = "lbl_paymentamount";
            this.lbl_paymentamount.Size = new System.Drawing.Size(69, 13);
            this.lbl_paymentamount.TabIndex = 12;
            this.lbl_paymentamount.Text = "Payment Amt";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(13, 36);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 13;
            this.label2.Text = "Name:";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(13, 56);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(44, 13);
            this.label3.TabIndex = 14;
            this.label3.Text = "Handle:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(12, 76);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(74, 13);
            this.label4.TabIndex = 15;
            this.label4.Text = "Contact email:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(12, 97);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(69, 13);
            this.label5.TabIndex = 16;
            this.label5.Text = "Paypal email:";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(12, 119);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(90, 13);
            this.label6.TabIndex = 17;
            this.label6.Text = "Payment Amount:";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(274, 36);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(41, 13);
            this.label7.TabIndex = 18;
            this.label7.Text = "Phone:";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(274, 56);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(58, 13);
            this.label8.TabIndex = 19;
            this.label8.Text = "Biz Phone:";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label9.Location = new System.Drawing.Point(277, 118);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(57, 13);
            this.label9.TabIndex = 20;
            this.label9.Text = "Balance:";
            // 
            // lbl_balance
            // 
            this.lbl_balance.AutoSize = true;
            this.lbl_balance.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lbl_balance.Location = new System.Drawing.Point(335, 119);
            this.lbl_balance.Name = "lbl_balance";
            this.lbl_balance.Size = new System.Drawing.Size(53, 13);
            this.lbl_balance.TabIndex = 21;
            this.lbl_balance.Text = "Balance";
            // 
            // btn_back
            // 
            this.btn_back.Location = new System.Drawing.Point(12, 535);
            this.btn_back.Name = "btn_back";
            this.btn_back.Size = new System.Drawing.Size(118, 38);
            this.btn_back.TabIndex = 22;
            this.btn_back.Text = "Back";
            this.btn_back.UseVisualStyleBackColor = true;
            this.btn_back.Click += new System.EventHandler(this.btn_back_Click);
            // 
            // bs_memberaccount
            // 
            this.bs_memberaccount.DataMember = "rows";
            this.bs_memberaccount.DataSource = typeof(DenhacClientAPI.ResponseObjects.GetMemberBalanceResponse);
            // 
            // transactiondateDataGridViewTextBoxColumn
            // 
            this.transactiondateDataGridViewTextBoxColumn.DataPropertyName = "transaction_date";
            this.transactiondateDataGridViewTextBoxColumn.HeaderText = "transaction_date";
            this.transactiondateDataGridViewTextBoxColumn.Name = "transactiondateDataGridViewTextBoxColumn";
            this.transactiondateDataGridViewTextBoxColumn.Width = 120;
            // 
            // amountDataGridViewTextBoxColumn
            // 
            this.amountDataGridViewTextBoxColumn.DataPropertyName = "amount";
            this.amountDataGridViewTextBoxColumn.HeaderText = "amount";
            this.amountDataGridViewTextBoxColumn.Name = "amountDataGridViewTextBoxColumn";
            this.amountDataGridViewTextBoxColumn.Width = 50;
            // 
            // typeDataGridViewTextBoxColumn
            // 
            this.typeDataGridViewTextBoxColumn.DataPropertyName = "type";
            this.typeDataGridViewTextBoxColumn.HeaderText = "type";
            this.typeDataGridViewTextBoxColumn.Name = "typeDataGridViewTextBoxColumn";
            this.typeDataGridViewTextBoxColumn.Width = 80;
            // 
            // notesDataGridViewTextBoxColumn
            // 
            this.notesDataGridViewTextBoxColumn.DataPropertyName = "notes";
            this.notesDataGridViewTextBoxColumn.HeaderText = "notes";
            this.notesDataGridViewTextBoxColumn.Name = "notesDataGridViewTextBoxColumn";
            this.notesDataGridViewTextBoxColumn.Width = 350;
            // 
            // MemberAccount
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(673, 585);
            this.Controls.Add(this.btn_back);
            this.Controls.Add(this.lbl_balance);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.lbl_paymentamount);
            this.Controls.Add(this.lbl_paypalemail);
            this.Controls.Add(this.lbl_contactemail);
            this.Controls.Add(this.lbl_adusername);
            this.Controls.Add(this.lbl_phone2);
            this.Controls.Add(this.lbl_phone);
            this.Controls.Add(this.lbl_id);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lbl_lastName);
            this.Controls.Add(this.lbl_firstName);
            this.Controls.Add(this.dgv_memberAccount);
            this.Name = "MemberAccount";
            this.Text = "MemberAccount";
            this.Load += new System.EventHandler(this.MemberAccount_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgv_memberAccount)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_memberaccount)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgv_memberAccount;
        private System.Windows.Forms.Label lbl_firstName;
        private System.Windows.Forms.Label lbl_lastName;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lbl_id;
        private System.Windows.Forms.Label lbl_phone;
        private System.Windows.Forms.Label lbl_phone2;
        private System.Windows.Forms.Label lbl_adusername;
        private System.Windows.Forms.Label lbl_contactemail;
        private System.Windows.Forms.Label lbl_paypalemail;
        private System.Windows.Forms.Label lbl_paymentamount;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.BindingSource bs_memberaccount;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label lbl_balance;
        private System.Windows.Forms.Button btn_back;
        private System.Windows.Forms.DataGridViewTextBoxColumn transactiondateDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn amountDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn typeDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn notesDataGridViewTextBoxColumn;
    }
}