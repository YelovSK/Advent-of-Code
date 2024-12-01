namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        /// <summary>
        /// Value is the number of occurences of the key. Like Python's Counter.
        /// </summary>
        public static Dictionary<TKey, int> ToCounter<TKey>(this IEnumerable<TKey> input) where TKey : notnull
        {
            return input.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
        }
    }
}