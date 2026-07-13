// Source Citation component to display source information for retrieved documents
import React from 'react';
interface SourceCitationProps {
  source: string;
  title: string;
  url: string;
}
const SourceCitation: React.FC<SourceCitationProps> = ({ source, title, url }) => {
  return (
    <div style={{ marginBottom: '10px' }}>
      <strong>{source}:</strong> <a href={url} target="_blank" rel="noopener noreferrer">{title}</a>
    </div>
  );
};
export default SourceCitation;  