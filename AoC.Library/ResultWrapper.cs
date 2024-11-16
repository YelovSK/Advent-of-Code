namespace AoC.Library;

public class ResultWrapper<TRes>
{
    public TRes Result { get; private init; } 
    public Exception Exception { get; private init; }
  
    public static ResultWrapper<TRes> Success(TRes result) => new ResultWrapper<TRes> { Result = result };
    public static ResultWrapper<TRes> Error(Exception ex) => new ResultWrapper<TRes> { Exception = ex };

    public override string? ToString()
    {
        return Exception?.Message ?? Result.ToString();
    }
}