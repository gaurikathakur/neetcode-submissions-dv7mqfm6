from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 1. Build the Graph and email-to-name mapping
        graph = defaultdict(list)
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for i in range(1, len(account)):
                email = account[i]
                # Map every email to its owner
                email_to_name[email] = name
                # Build undirected edges between the first email and others
                if i > 1:
                    prev_email = account[i-1]
                    graph[prev_email].append(email)
                    graph[email].append(prev_email)
        
        # 2. Traverse connected components using BFS
        visited = set()
        result = []
        
        for email in email_to_name:
            if email not in visited:
                visited.add(email)
                component = []
                queue = deque([email])
                
                while queue:
                    curr = queue.popleft()
                    component.append(curr)
                    
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                # 3. Format the result
                # Sort emails and prepend the name
                result.append([email_to_name[email]] + sorted(component))
                
        return result



        
        