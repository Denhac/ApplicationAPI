using DenhacClientAPI.ResponseObjects;
using Newtonsoft.Json;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static DenhacResponse GetPaymentTypesService()
        {
            var resultStr = CallGet(hostName + "/getpaymenttypes");
            GetPaymentTypesResponse responseObj = JsonConvert.DeserializeObject<GetPaymentTypesResponse>(resultStr);

            if (responseObj.rows != null)
                responseObj.transactionStatus = true;
            else
                responseObj.transactionStatus = false;

            return responseObj;
        }
    }
}
