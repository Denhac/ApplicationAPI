using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

using System.Collections.Generic;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse LoginService()
        {
            var postData = new List<KeyValuePair<string, string>>();
            postData.Add(new KeyValuePair<string, string>("username", userName));
            postData.Add(new KeyValuePair<string, string>("password", password));

            var resultStr = CallPost(hostName + "/login", postData);
            LoginResponse responseObj = JsonConvert.DeserializeObject<LoginResponse>(resultStr);

            if (responseObj.logged_in != null && responseObj.logged_in.Equals("True"))
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
