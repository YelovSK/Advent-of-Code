using System.Numerics;

namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        /// <summary>
        /// Value is the number of occurences of the key. Like Python's Counter.
        /// </summary>
        public static Dictionary<TKey, int> ToCounter<TKey>(this IEnumerable<TKey> input) where TKey : notnull
        {
            return input.ToCounter<TKey, int>();
        }

        /// <summary>
        /// Value is the number of occurences of the key. Like Python's Counter.
        /// </summary>
        /// <typeparam name="TVal">Numeric type for the count. Basically if int it not enough you can use e.g. long</typeparam>
        public static Dictionary<TKey, TVal> ToCounter<TKey, TVal>(this IEnumerable<TKey> input)
            where TKey : notnull
            where TVal : INumber<TVal>
        {
            return input.GroupBy(x => x).ToDictionary(g => g.Key, g => (TVal)Convert.ChangeType(g.Count(), typeof(TVal)));
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

        public static IEnumerable<IGrouping<TSource, TSource>> Group<TSource>(this IEnumerable<TSource> enumerable)
        {
            return enumerable.GroupBy(_ => _);
        }
    }
}