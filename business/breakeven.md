# Breakeven Analysis
## Cost per Active User
We estimate the following costs for role-sentry:
* Compute: $0.05 per user per month (assuming 10% average utilization of a $5/month server)
* Storage: $0.01 per user per month (assuming 100MB storage per user at $0.10/GB-month)
* Bandwidth: $0.005 per user per month (assuming 100MB transfer per user at $0.05/GB)
Total cost per active user: $0.065 per month

## Pricing Tiers
We propose the following pricing tiers for role-sentry:
* **Basic**: $9.99/month (100 users, 1GB storage, 1GB bandwidth)
* **Pro**: $29.99/month (500 users, 5GB storage, 5GB bandwidth)
* **Enterprise**: $99.99/month (2000 users, 20GB storage, 20GB bandwidth)

## Customer Acquisition Cost (CAC) Range
Based on industry benchmarks, we estimate the CAC range for role-sentry to be between $15 and $30 per user.

## Lifetime Value (LTV) Estimate
Assuming an average user lifetime of 12 months and an average revenue per user (ARPU) of $19.99 ( weighted average of pricing tiers), we estimate the LTV to be:
LTV = ARPU x user lifetime = $19.99 x 12 = $239.88

## Break-even Users Count
To calculate the break-even point, we need to consider the CAC and LTV. Assuming a CAC of $22.50 (midpoint of the estimated range), we can calculate the break-even point as follows:
Break-even point = CAC / (LTV - CAC) = $22.50 / ($239.88 - $22.50) = 0.105 or 10.5% of total users
Break-even users count = Total users x break-even point
We will calculate this once we have the total users count.

## Path to $10K MRR
To reach $10,000 MRR, we can estimate the required number of users for each tier:
* **Basic**: $9.99/month x number of users = $10,000
Number of users = $10,000 / $9.99 ≈ 1001 users (not feasible with basic tier alone)
* **Pro**: $29.99/month x number of users = $10,000
Number of users = $10,000 / $29.99 ≈ 334 users (more feasible with pro tier)
* **Enterprise**: $99.99/month x number of users = $10,000
Number of users = $10,000 / $99.99 ≈ 100 users (most feasible with enterprise tier)
A combination of **Pro** and **Enterprise** tiers can help us reach $10,000 MRR:
* 200 **Pro** users = $29.99 x 200 = $5,998
* 50 **Enterprise** users = $99.99 x 50 = $4,995
Total MRR = $5,998 + $4,995 = $10,993
This combination will put us over the $10,000 MRR target.