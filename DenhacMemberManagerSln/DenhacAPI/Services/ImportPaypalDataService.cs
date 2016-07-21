using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

using System.Collections.Generic;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse ImportPaypalDataService(string data)
        {
            var postData = new List<KeyValuePair<string, string>>();
            postData.Add(new KeyValuePair<string, string>("filedata", data));
            
            var resultStr = CallPost(hostName + "/importpaypaldata", postData);
            ImportPaypalDataResponse responseObj = JsonConvert.DeserializeObject<ImportPaypalDataResponse>(resultStr);

            if (responseObj.response != null)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
