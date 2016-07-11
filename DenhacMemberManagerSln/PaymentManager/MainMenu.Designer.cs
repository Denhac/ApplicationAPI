namespace PaymentManager
{
    partial class MainMenu
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
            this.btn_memberPayment = new System.Windows.Forms.Button();
            this.txt_username = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.txt_password = new System.Windows.Forms.TextBox();
            this.btn_testConnection = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.txt_server = new System.Windows.Forms.TextBox();
            this.btn_logout = new System.Windows.Forms.Button();
            this.btn_multiPayment = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.btn_importpaypal = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btn_memberPayment
            // 
            this.btn_memberPayment.Enabled = false;
            this.btn_memberPayment.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_memberPayment.Location = new System.Drawing.Point(24, 307);
            this.btn_memberPayment.Name = "btn_memberPayment";
            this.btn_memberPayment.Size = new System.Drawing.Size(186, 59);
            this.btn_memberPayment.TabIndex = 0;
            this.btn_memberPayment.Text = "ENTER PAYMENT/ ADJUSTMENT";
            this.btn_memberPayment.UseVisualStyleBackColor = true;
            this.btn_memberPayment.Click += new System.EventHandler(this.btn_memberPayment_Click);
            // 
            // txt_username
            // 
            this.txt_username.Location = new System.Drawing.Point(12, 74);
            this.txt_username.Name = "txt_username";
            this.txt_username.Size = new System.Drawing.Size(208, 20);
            this.txt_username.TabIndex = 1;
            this.txt_username.Text = "digimonkey";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 58);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Username:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 109);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(56, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Password:";
            // 
            // txt_password
            // 
            this.txt_password.Location = new System.Drawing.Point(12, 126);
            this.txt_password.Name = "txt_password";
            this.txt_password.Size = new System.Drawing.Size(208, 20);
            this.txt_password.TabIndex = 4;
            this.txt_password.UseSystemPasswordChar = true;
            // 
            // btn_testConnection
            // 
            this.btn_testConnection.Location = new System.Drawing.Point(12, 164);
            this.btn_testConnection.Name = "btn_testConnection";
            this.btn_testConnection.Size = new System.Drawing.Size(208, 23);
            this.btn_testConnection.TabIndex = 5;
            this.btn_testConnection.Text = "TEST CONNECTION / LOGIN";
            this.btn_testConnection.UseVisualStyleBackColor = true;
            this.btn_testConnection.Click += new System.EventHandler(this.btn_testConnection_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(13, 9);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(61, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "API Server:";
            // 
            // txt_server
            // 
            this.txt_server.Location = new System.Drawing.Point(12, 25);
            this.txt_server.Name = "txt_server";
            this.txt_server.Size = new System.Drawing.Size(208, 20);
            this.txt_server.TabIndex = 6;
            this.txt_server.Text = "http://10.0.101.248/";
            // 
            // btn_logout
            // 
            this.btn_logout.Enabled = false;
            this.btn_logout.Location = new System.Drawing.Point(12, 475);
            this.btn_logout.Name = "btn_logout";
            this.btn_logout.Size = new System.Drawing.Size(208, 23);
            this.btn_logout.TabIndex = 8;
            this.btn_logout.Text = "LOGOUT";
            this.btn_logout.UseVisualStyleBackColor = true;
            this.btn_logout.Click += new System.EventHandler(this.btn_logout_Click);
            // 
            // btn_multiPayment
            // 
            this.btn_multiPayment.Enabled = false;
            this.btn_multiPayment.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_multiPayment.Location = new System.Drawing.Point(24, 231);
            this.btn_multiPayment.Name = "btn_multiPayment";
            this.btn_multiPayment.Size = new System.Drawing.Size(186, 59);
            this.btn_multiPayment.TabIndex = 9;
            this.btn_multiPayment.Text = "VIEW BALANCES";
            this.btn_multiPayment.UseVisualStyleBackColor = true;
            this.btn_multiPayment.Click += new System.EventHandler(this.btn_multiPayment_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(35, 501);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(154, 15);
            this.label4.TabIndex = 10;
            this.label4.Text = "Powered by Digimonkey";
            // 
            // btn_importpaypal
            // 
            this.btn_importpaypal.Enabled = false;
            this.btn_importpaypal.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btn_importpaypal.Location = new System.Drawing.Point(24, 381);
            this.btn_importpaypal.Name = "btn_importpaypal";
            this.btn_importpaypal.Size = new System.Drawing.Size(186, 59);
            this.btn_importpaypal.TabIndex = 11;
            this.btn_importpaypal.Text = "IMPORT PAYPAL STATEMENT";
            this.btn_importpaypal.UseVisualStyleBackColor = true;
            // 
            // MainMenu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(234, 525);
            this.Controls.Add(this.btn_importpaypal);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.btn_multiPayment);
            this.Controls.Add(this.btn_logout);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txt_server);
            this.Controls.Add(this.btn_testConnection);
            this.Controls.Add(this.txt_password);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txt_username);
            this.Controls.Add(this.btn_memberPayment);
            this.Name = "MainMenu";
            this.Text = "Main Menu";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btn_memberPayment;
        private System.Windows.Forms.TextBox txt_username;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txt_password;
        private System.Windows.Forms.Button btn_testConnection;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txt_server;
        private System.Windows.Forms.Button btn_logout;
        private System.Windows.Forms.Button btn_multiPayment;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btn_importpaypal;
    }
}

