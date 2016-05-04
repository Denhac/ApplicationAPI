using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse GetOpenBalanceService()
        {
            var resultStr = CallGet(hostName + "/getopenbalances");
            OpenBalanceResponse responseObj = JsonConvert.DeserializeObject<OpenBalanceResponse>(resultStr);

            if (responseObj.rows != null)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
