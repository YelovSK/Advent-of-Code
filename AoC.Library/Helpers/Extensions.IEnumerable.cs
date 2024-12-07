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

        public static IEnumerable<List<T>> PermutationsWithRepetition<T>(this IEnumerable<T> items, int sampleSize)
        {
            if (sampleSize == 1)
            {
                foreach (var item in items)
                {
                    yield return new List<T> { item };
                }
            }
            else
            {
                foreach (var item in items)
                {
                    foreach (var perm in PermutationsWithRepetition(items, sampleSize - 1))
                    {
                        var newPerm = new List<T> { item };
                        newPerm.AddRange(perm);
                        yield return newPerm;
                    }
                }
            }
        }
    }
}