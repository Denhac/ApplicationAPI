using System.Collections.Generic;
using System.Net;
using System.Net.Http;

namespace DenhacClientAPI.Services
{
    public static partial class DenhacService
    {
        public static string hostName;
        public static string userName;
        public static string password;
        private static CookieContainer cookies;

        private static string CallGet(string URI)
        {
            using (HttpClientHandler httpHandler = new HttpClientHandler
            {
                AllowAutoRedirect = true,
                UseCookies = true
            })
            {
                if (cookies != null)
                {
                    httpHandler.CookieContainer = cookies;
                }
                else
                {
                    httpHandler.CookieContainer = new CookieContainer();
                }

                using (HttpClient client = new HttpClient(httpHandler))
                {
                    using (HttpResponseMessage response = client.GetAsync(URI).Result)
                    {
                        return response.Content.ReadAsStringAsync().Result;
                    }
                }
            }
        }

        private static string CallPost(string URI, List<KeyValuePair<string, string>> postData)
        {
            using (HttpContent content = new FormUrlEncodedContent(postData))
            {
                using (HttpClientHandler httpHandler = new HttpClientHandler
                {
                    AllowAutoRedirect = true,
                    UseCookies = true
                })
                {
                    if (cookies != null)
                    {
                        httpHandler.CookieContainer = cookies;
                    }
                    else
                    {
                        httpHandler.CookieContainer = new CookieContainer();
                    }

                    using (HttpClient client = new HttpClient(httpHandler))
                    {
                        // Using .Result like this turns it into a synchronous (blocking) call.
                        // Since we need to check all response anyway, this saves Task checking from more complicated async code
                        using (HttpResponseMessage response = client.PostAsync(URI, content).Result)
                        {
                            if (response.IsSuccessStatusCode)
                            {
                                cookies = httpHandler.CookieContainer;
                                return response.Content.ReadAsStringAsync().Result;
                            }
                            else
                            {
                                return null;
                            }
                        }
                    }
                }
            }
        }
    }
}
