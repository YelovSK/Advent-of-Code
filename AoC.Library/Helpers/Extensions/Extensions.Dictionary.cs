using System.Collections.Concurrent;

namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        public static ConcurrentDictionary<TKey, TVal> ToConcurrent<TKey, TVal>(this Dictionary<TKey, TVal> dict) where TKey : notnull
        {
            return new ConcurrentDictionary<TKey, TVal>(dict);
        }
    }
}
