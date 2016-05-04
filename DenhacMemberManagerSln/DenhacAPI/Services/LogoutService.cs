using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse LogoutService()
        {
            var resultStr = CallGet(hostName + "/logout");
            LogoutResponse responseObj = JsonConvert.DeserializeObject<LogoutResponse>(resultStr);

            if (responseObj.logged_out != null && responseObj.logged_out.Equals("True"))
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
