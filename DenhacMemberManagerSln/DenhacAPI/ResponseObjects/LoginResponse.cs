using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DenhacClientAPI.ResponseObjects
{
    class LoginResponse : DenhacResponse
    {
        public string username { get; set; }
        public string logged_in { get; set; }
    }
}
