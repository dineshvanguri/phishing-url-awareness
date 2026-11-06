
# Test Samples

| No. | Sample URL | Expected Result |
|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs |
| 2 | http://192.0.2.10/account | IP address and HTTP warnings |
| 3 | http://example.com@sample.invalid/login | @ symbol and HTTP warnings |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments warning |
| 5 | https://xn--example.invalid/ | Punycode warning |

## Test Results

Record the actual result and mark each test PASS or FAIL after running it.

| Test | Actual Result | Status |
|---|---|---|
| 1 | No listed warning signs found | PASS |
| 2 | IP address and HTTP warnings | PASS |
| 3 | @ symbol and HTTP warnings | PASS |
| 4 | Many hostname segments warning | PASS |
| 5 | Punycode warning | PASS |
