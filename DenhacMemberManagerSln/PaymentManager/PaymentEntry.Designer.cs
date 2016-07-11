namespace PaymentManager
{
    partial class PaymentEntry
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
            this.txt_search = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.btn_back1 = new System.Windows.Forms.Button();
            this.txt_member = new System.Windows.Forms.TextBox();
            this.dgv_searchResults = new System.Windows.Forms.DataGridView();
            this.idDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.lastNameDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.firstNameDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.gnuCashIdDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.paymentAmountDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.activeDataGridViewCheckBoxColumn = new System.Windows.Forms.DataGridViewCheckBoxColumn();
            this.onAutoPayDataGridViewCheckBoxColumn = new System.Windows.Forms.DataGridViewCheckBoxColumn();
            this.contactemailDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.paypalemailDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.bs_searchMemberResponse = new System.Windows.Forms.BindingSource(this.components);
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.cb_paymentType = new System.Windows.Forms.ComboBox();
            this.bs_paymentTypesResponse = new System.Windows.Forms.BindingSource(this.components);
            this.txt_memoNotes = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.btn_submit = new System.Windows.Forms.Button();
            this.label7 = new System.Windows.Forms.Label();
            this.txt_amount = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dgv_searchResults)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_searchMemberResponse)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_paymentTypesResponse)).BeginInit();
            this.SuspendLayout();
            // 
            // txt_search
            // 
            this.txt_search.Location = new System.Drawing.Point(15, 51);
            this.txt_search.Name = "txt_search";
            this.txt_search.Size = new System.Drawing.Size(170, 20);
            this.txt_search.TabIndex = 0;
            this.txt_search.TextChanged += new System.EventHandler(this.txt_search_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(12, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(95, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Search Member";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(203, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(53, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Results:";
            // 
            // btn_back1
            // 
            this.btn_back1.Location = new System.Drawing.Point(12, 411);
            this.btn_back1.Name = "btn_back1";
            this.btn_back1.Size = new System.Drawing.Size(75, 23);
            this.btn_back1.TabIndex = 4;
            this.btn_back1.Text = "BACK";
            this.btn_back1.UseVisualStyleBackColor = true;
            this.btn_back1.Click += new System.EventHandler(this.btn_back1_Click);
            // 
            // txt_member
            // 
            this.txt_member.Location = new System.Drawing.Point(114, 271);
            this.txt_member.Name = "txt_member";
            this.txt_member.ReadOnly = true;
            this.txt_member.Size = new System.Drawing.Size(170, 20);
            this.txt_member.TabIndex = 5;
            // 
            // dgv_searchResults
            // 
            this.dgv_searchResults.AllowUserToAddRows = false;
            this.dgv_searchResults.AllowUserToDeleteRows = false;
            this.dgv_searchResults.AllowUserToResizeRows = false;
            this.dgv_searchResults.AutoGenerateColumns = false;
            this.dgv_searchResults.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgv_searchResults.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.idDataGridViewTextBoxColumn,
            this.lastNameDataGridViewTextBoxColumn,
            this.firstNameDataGridViewTextBoxColumn,
            this.gnuCashIdDataGridViewTextBoxColumn,
            this.paymentAmountDataGridViewTextBoxColumn,
            this.activeDataGridViewCheckBoxColumn,
            this.onAutoPayDataGridViewCheckBoxColumn,
            this.contactemailDataGridViewTextBoxColumn,
            this.paypalemailDataGridViewTextBoxColumn});
            this.dgv_searchResults.DataSource = this.bs_searchMemberResponse;
            this.dgv_searchResults.Location = new System.Drawing.Point(206, 29);
            this.dgv_searchResults.Name = "dgv_searchResults";
            this.dgv_searchResults.ReadOnly = true;
            this.dgv_searchResults.Size = new System.Drawing.Size(544, 197);
            this.dgv_searchResults.TabIndex = 6;
            this.dgv_searchResults.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgv_searchResults_CellClick);
            // 
            // idDataGridViewTextBoxColumn
            // 
            this.idDataGridViewTextBoxColumn.DataPropertyName = "id";
            this.idDataGridViewTextBoxColumn.HeaderText = "id";
            this.idDataGridViewTextBoxColumn.Name = "idDataGridViewTextBoxColumn";
            this.idDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // lastNameDataGridViewTextBoxColumn
            // 
            this.lastNameDataGridViewTextBoxColumn.DataPropertyName = "lastName";
            this.lastNameDataGridViewTextBoxColumn.HeaderText = "lastName";
            this.lastNameDataGridViewTextBoxColumn.Name = "lastNameDataGridViewTextBoxColumn";
            this.lastNameDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // firstNameDataGridViewTextBoxColumn
            // 
            this.firstNameDataGridViewTextBoxColumn.DataPropertyName = "firstName";
            this.firstNameDataGridViewTextBoxColumn.HeaderText = "firstName";
            this.firstNameDataGridViewTextBoxColumn.Name = "firstNameDataGridViewTextBoxColumn";
            this.firstNameDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // gnuCashIdDataGridViewTextBoxColumn
            // 
            this.gnuCashIdDataGridViewTextBoxColumn.DataPropertyName = "gnuCashId";
            this.gnuCashIdDataGridViewTextBoxColumn.HeaderText = "gnuCashId";
            this.gnuCashIdDataGridViewTextBoxColumn.Name = "gnuCashIdDataGridViewTextBoxColumn";
            this.gnuCashIdDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // paymentAmountDataGridViewTextBoxColumn
            // 
            this.paymentAmountDataGridViewTextBoxColumn.DataPropertyName = "paymentAmount";
            this.paymentAmountDataGridViewTextBoxColumn.HeaderText = "paymentAmount";
            this.paymentAmountDataGridViewTextBoxColumn.Name = "paymentAmountDataGridViewTextBoxColumn";
            this.paymentAmountDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // activeDataGridViewCheckBoxColumn
            // 
            this.activeDataGridViewCheckBoxColumn.DataPropertyName = "active";
            this.activeDataGridViewCheckBoxColumn.HeaderText = "active";
            this.activeDataGridViewCheckBoxColumn.Name = "activeDataGridViewCheckBoxColumn";
            this.activeDataGridViewCheckBoxColumn.ReadOnly = true;
            // 
            // onAutoPayDataGridViewCheckBoxColumn
            // 
            this.onAutoPayDataGridViewCheckBoxColumn.DataPropertyName = "onAutoPay";
            this.onAutoPayDataGridViewCheckBoxColumn.HeaderText = "onAutoPay";
            this.onAutoPayDataGridViewCheckBoxColumn.Name = "onAutoPayDataGridViewCheckBoxColumn";
            this.onAutoPayDataGridViewCheckBoxColumn.ReadOnly = true;
            // 
            // contactemailDataGridViewTextBoxColumn
            // 
            this.contactemailDataGridViewTextBoxColumn.DataPropertyName = "contact_email";
            this.contactemailDataGridViewTextBoxColumn.HeaderText = "contact_email";
            this.contactemailDataGridViewTextBoxColumn.Name = "contactemailDataGridViewTextBoxColumn";
            this.contactemailDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // paypalemailDataGridViewTextBoxColumn
            // 
            this.paypalemailDataGridViewTextBoxColumn.DataPropertyName = "paypal_email";
            this.paypalemailDataGridViewTextBoxColumn.HeaderText = "paypal_email";
            this.paypalemailDataGridViewTextBoxColumn.Name = "paypalemailDataGridViewTextBoxColumn";
            this.paypalemailDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // bs_searchMemberResponse
            // 
            this.bs_searchMemberResponse.DataMember = "rows";
            this.bs_searchMemberResponse.DataSource = typeof(DenhacClientAPI.ResponseObjects.SearchMemberResponse);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(111, 255);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(55, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Member:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(12, 29);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(115, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "(Type at least 3 chars):";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(111, 300);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(91, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Payment Type:";
            // 
            // cb_paymentType
            // 
            this.cb_paymentType.DataSource = this.bs_paymentTypesResponse;
            this.cb_paymentType.DisplayMember = "description";
            this.cb_paymentType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cb_paymentType.FormattingEnabled = true;
            this.cb_paymentType.Location = new System.Drawing.Point(114, 317);
            this.cb_paymentType.Name = "cb_paymentType";
            this.cb_paymentType.Size = new System.Drawing.Size(170, 21);
            this.cb_paymentType.TabIndex = 10;
            // 
            // bs_paymentTypesResponse
            // 
            this.bs_paymentTypesResponse.DataSource = typeof(DenhacClientAPI.ResponseObjects.PaymentType);
            // 
            // txt_memoNotes
            // 
            this.txt_memoNotes.Location = new System.Drawing.Point(305, 271);
            this.txt_memoNotes.Multiline = true;
            this.txt_memoNotes.Name = "txt_memoNotes";
            this.txt_memoNotes.Size = new System.Drawing.Size(209, 112);
            this.txt_memoNotes.TabIndex = 11;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(302, 255);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(83, 13);
            this.label6.TabIndex = 12;
            this.label6.Text = "Memo/Notes:";
            // 
            // btn_submit
            // 
            this.btn_submit.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_submit.Location = new System.Drawing.Point(547, 271);
            this.btn_submit.Name = "btn_submit";
            this.btn_submit.Size = new System.Drawing.Size(112, 112);
            this.btn_submit.TabIndex = 13;
            this.btn_submit.Text = "SUBMIT";
            this.btn_submit.UseVisualStyleBackColor = true;
            this.btn_submit.Click += new System.EventHandler(this.btn_submit_Click);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.Location = new System.Drawing.Point(111, 347);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(53, 13);
            this.label7.TabIndex = 14;
            this.label7.Text = "Amount:";
            // 
            // txt_amount
            // 
            this.txt_amount.Location = new System.Drawing.Point(114, 363);
            this.txt_amount.Name = "txt_amount";
            this.txt_amount.Size = new System.Drawing.Size(170, 20);
            this.txt_amount.TabIndex = 15;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(111, 386);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(139, 13);
            this.label8.TabIndex = 16;
            this.label8.Text = "(+ for Payment, - for Charge)";
            // 
            // PaymentEntry
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(765, 446);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.txt_amount);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.btn_submit);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.txt_memoNotes);
            this.Controls.Add(this.cb_paymentType);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.dgv_searchResults);
            this.Controls.Add(this.txt_member);
            this.Controls.Add(this.btn_back1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txt_search);
            this.Name = "PaymentEntry";
            this.Text = "Member Payment";
            this.Load += new System.EventHandler(this.PaymentEntry_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgv_searchResults)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_searchMemberResponse)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_paymentTypesResponse)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txt_search;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button btn_back1;
        private System.Windows.Forms.TextBox txt_member;
        private System.Windows.Forms.BindingSource bs_searchMemberResponse;
        private System.Windows.Forms.DataGridViewTextBoxColumn birthdateDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn streetAddress1DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn streetAddress2DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn cityDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn zipCodeDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn phoneNumberDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn businessNumberDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerContact1DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerPhone1DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerAddress1DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerRelation1DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerContact2DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerPhone2DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerAddress2DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn emerRelation2DataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn medicalConditionListDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn isManagerDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn isAdminDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn adusernameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn joindateDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn proxcardidDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn driverlicenseDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridView dgv_searchResults;
        private System.Windows.Forms.DataGridViewTextBoxColumn idDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn lastNameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn firstNameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn middleInitialDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn gnuCashIdDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn paymentAmountDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn activeDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn onAutoPayDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn contactemailDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn paypalemailDataGridViewTextBoxColumn;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.ComboBox cb_paymentType;
        private System.Windows.Forms.BindingSource bs_paymentTypesResponse;
        private System.Windows.Forms.TextBox txt_memoNotes;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Button btn_submit;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox txt_amount;
        private System.Windows.Forms.Label label8;
    }
}