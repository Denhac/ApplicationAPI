namespace PaymentManager
{
    partial class OpenBalances
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
            this.btn_back = new System.Windows.Forms.Button();
            this.dgv_openBalances = new System.Windows.Forms.DataGridView();
            this.phoneNumber = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.ad_username = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.label1 = new System.Windows.Forms.Label();
            this.btn_viewAccount = new System.Windows.Forms.Button();
            this.balanceDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.idDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.lastNameDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.firstNameDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.paymentAmountDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.activeDataGridViewCheckBoxColumn = new System.Windows.Forms.DataGridViewCheckBoxColumn();
            this.onAutoPayDataGridViewCheckBoxColumn = new System.Windows.Forms.DataGridViewCheckBoxColumn();
            this.contactemailDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.paypalemailDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.bs_openBalanceResponse = new System.Windows.Forms.BindingSource(this.components);
            ((System.ComponentModel.ISupportInitialize)(this.dgv_openBalances)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_openBalanceResponse)).BeginInit();
            this.SuspendLayout();
            // 
            // btn_back
            // 
            this.btn_back.Location = new System.Drawing.Point(13, 439);
            this.btn_back.Name = "btn_back";
            this.btn_back.Size = new System.Drawing.Size(75, 23);
            this.btn_back.TabIndex = 0;
            this.btn_back.Text = "Back";
            this.btn_back.UseVisualStyleBackColor = true;
            this.btn_back.Click += new System.EventHandler(this.btn_back_Click);
            // 
            // dgv_openBalances
            // 
            this.dgv_openBalances.AutoGenerateColumns = false;
            this.dgv_openBalances.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgv_openBalances.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.balanceDataGridViewTextBoxColumn,
            this.idDataGridViewTextBoxColumn,
            this.lastNameDataGridViewTextBoxColumn,
            this.firstNameDataGridViewTextBoxColumn,
            this.paymentAmountDataGridViewTextBoxColumn,
            this.activeDataGridViewCheckBoxColumn,
            this.onAutoPayDataGridViewCheckBoxColumn,
            this.contactemailDataGridViewTextBoxColumn,
            this.paypalemailDataGridViewTextBoxColumn,
            this.phoneNumber,
            this.ad_username});
            this.dgv_openBalances.DataSource = this.bs_openBalanceResponse;
            this.dgv_openBalances.Location = new System.Drawing.Point(12, 29);
            this.dgv_openBalances.Name = "dgv_openBalances";
            this.dgv_openBalances.Size = new System.Drawing.Size(1085, 380);
            this.dgv_openBalances.TabIndex = 1;
            this.dgv_openBalances.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dgv_openBalances_CellClick);
            this.dgv_openBalances.DoubleClick += new System.EventHandler(this.dgv_openBalances_DoubleClick);
            // 
            // phoneNumber
            // 
            this.phoneNumber.DataPropertyName = "phoneNumber";
            this.phoneNumber.HeaderText = "phoneNumber";
            this.phoneNumber.Name = "phoneNumber";
            // 
            // ad_username
            // 
            this.ad_username.DataPropertyName = "ad_username";
            this.ad_username.HeaderText = "ad_username";
            this.ad_username.Name = "ad_username";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(9, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(175, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Members with open balances:";
            // 
            // btn_viewAccount
            // 
            this.btn_viewAccount.Location = new System.Drawing.Point(959, 415);
            this.btn_viewAccount.Name = "btn_viewAccount";
            this.btn_viewAccount.Size = new System.Drawing.Size(138, 48);
            this.btn_viewAccount.TabIndex = 3;
            this.btn_viewAccount.Text = "View Account";
            this.btn_viewAccount.UseVisualStyleBackColor = true;
            this.btn_viewAccount.Click += new System.EventHandler(this.btn_viewAccount_Click);
            // 
            // balanceDataGridViewTextBoxColumn
            // 
            this.balanceDataGridViewTextBoxColumn.DataPropertyName = "balance";
            this.balanceDataGridViewTextBoxColumn.HeaderText = "balance";
            this.balanceDataGridViewTextBoxColumn.Name = "balanceDataGridViewTextBoxColumn";
            this.balanceDataGridViewTextBoxColumn.Width = 50;
            // 
            // idDataGridViewTextBoxColumn
            // 
            this.idDataGridViewTextBoxColumn.DataPropertyName = "id";
            this.idDataGridViewTextBoxColumn.HeaderText = "id";
            this.idDataGridViewTextBoxColumn.Name = "idDataGridViewTextBoxColumn";
            this.idDataGridViewTextBoxColumn.Width = 30;
            // 
            // lastNameDataGridViewTextBoxColumn
            // 
            this.lastNameDataGridViewTextBoxColumn.DataPropertyName = "lastName";
            this.lastNameDataGridViewTextBoxColumn.HeaderText = "lastName";
            this.lastNameDataGridViewTextBoxColumn.Name = "lastNameDataGridViewTextBoxColumn";
            this.lastNameDataGridViewTextBoxColumn.Width = 120;
            // 
            // firstNameDataGridViewTextBoxColumn
            // 
            this.firstNameDataGridViewTextBoxColumn.DataPropertyName = "firstName";
            this.firstNameDataGridViewTextBoxColumn.HeaderText = "firstName";
            this.firstNameDataGridViewTextBoxColumn.Name = "firstNameDataGridViewTextBoxColumn";
            // 
            // paymentAmountDataGridViewTextBoxColumn
            // 
            this.paymentAmountDataGridViewTextBoxColumn.DataPropertyName = "paymentAmount";
            this.paymentAmountDataGridViewTextBoxColumn.HeaderText = "Amount";
            this.paymentAmountDataGridViewTextBoxColumn.Name = "paymentAmountDataGridViewTextBoxColumn";
            this.paymentAmountDataGridViewTextBoxColumn.Width = 50;
            // 
            // activeDataGridViewCheckBoxColumn
            // 
            this.activeDataGridViewCheckBoxColumn.DataPropertyName = "active";
            this.activeDataGridViewCheckBoxColumn.HeaderText = "active";
            this.activeDataGridViewCheckBoxColumn.Name = "activeDataGridViewCheckBoxColumn";
            this.activeDataGridViewCheckBoxColumn.Width = 40;
            // 
            // onAutoPayDataGridViewCheckBoxColumn
            // 
            this.onAutoPayDataGridViewCheckBoxColumn.DataPropertyName = "onAutoPay";
            this.onAutoPayDataGridViewCheckBoxColumn.HeaderText = "AutoPay";
            this.onAutoPayDataGridViewCheckBoxColumn.Name = "onAutoPayDataGridViewCheckBoxColumn";
            this.onAutoPayDataGridViewCheckBoxColumn.Width = 40;
            // 
            // contactemailDataGridViewTextBoxColumn
            // 
            this.contactemailDataGridViewTextBoxColumn.DataPropertyName = "contact_email";
            this.contactemailDataGridViewTextBoxColumn.HeaderText = "contact_email";
            this.contactemailDataGridViewTextBoxColumn.Name = "contactemailDataGridViewTextBoxColumn";
            this.contactemailDataGridViewTextBoxColumn.Width = 200;
            // 
            // paypalemailDataGridViewTextBoxColumn
            // 
            this.paypalemailDataGridViewTextBoxColumn.DataPropertyName = "paypal_email";
            this.paypalemailDataGridViewTextBoxColumn.HeaderText = "paypal_email";
            this.paypalemailDataGridViewTextBoxColumn.Name = "paypalemailDataGridViewTextBoxColumn";
            this.paypalemailDataGridViewTextBoxColumn.Width = 200;
            // 
            // bs_openBalanceResponse
            // 
            this.bs_openBalanceResponse.DataMember = "rows";
            this.bs_openBalanceResponse.DataSource = typeof(DenhacClientAPI.ResponseObjects.OpenBalanceResponse);
            // 
            // OpenBalances
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1104, 475);
            this.Controls.Add(this.btn_viewAccount);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.dgv_openBalances);
            this.Controls.Add(this.btn_back);
            this.Name = "OpenBalances";
            this.Text = "Open Balances";
            this.Load += new System.EventHandler(this.MultiplePayments_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dgv_openBalances)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bs_openBalanceResponse)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_back;
        private System.Windows.Forms.DataGridView dgv_openBalances;
        private System.Windows.Forms.BindingSource bs_openBalanceResponse;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridViewTextBoxColumn balanceDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn idDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn lastNameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn firstNameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn paymentAmountDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn activeDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewCheckBoxColumn onAutoPayDataGridViewCheckBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn contactemailDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn paypalemailDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn phoneNumber;
        private System.Windows.Forms.DataGridViewTextBoxColumn ad_username;
        private System.Windows.Forms.Button btn_viewAccount;
    }
}