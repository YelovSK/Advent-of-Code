using System.Diagnostics;

namespace AoC.Library;

public static class Solver
{
   public static ResultWrapper<Solution> Solve(BaseDay day, SolveOptions options)
   {
       var solution = new Solution();

       try
       {
           if (options.SolvePart1)
           {
               var start = Stopwatch.GetTimestamp();
               solution.Part1Result = day.Part1();
               solution.Part1Elapsed = Stopwatch.GetElapsedTime(start);
           }

           if (options.SolvePart2)
           {
               var start = Stopwatch.GetTimestamp();
               solution.Part2Result = day.Part2();
               solution.Part2Elapsed = Stopwatch.GetElapsedTime(start);          
           }
       }
       catch (Exception e)
       {
           return ResultWrapper<Solution>.Error(e);
       }

       return ResultWrapper<Solution>.Success(solution);
   } 
   
   public static ResultWrapper<Solution> SolvePart1(BaseDay day) => Solve(day, new SolveOptions(true, false));
   public static ResultWrapper<Solution> SolvePart2(BaseDay day) => Solve(day, new SolveOptions(false, true));
}